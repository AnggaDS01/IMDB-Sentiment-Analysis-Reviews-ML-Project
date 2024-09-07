from imbd_sentiment.logger import logging
from imbd_sentiment.constants import LABEL, FEATURE
from imbd_sentiment.exception import CustomException
from imbd_sentiment.entity.config_entity import ModelTrainerConfig
from imbd_sentiment.entity.artifact_entity import ModelTrainerArtifacts, DataTransformationArtifacts
from imbd_sentiment.ml.model_architecture import build_lstm_model
from imbd_sentiment.utils import DatasetSplitter
from imbd_sentiment.utils import save_object

from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore
from tensorflow.keras.preprocessing.text import Tokenizer # type: ignore

import os 
import sys
import pickle
import pandas as pd
import tensorflow as tf


class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig, data_transformation_artifacts: DataTransformationArtifacts):
        self.model_trainer_config = model_trainer_config
        self.data_transformation_artifacts = data_transformation_artifacts
        logging.info(f"ModelTrainer initialized with config: {model_trainer_config} and data artifacts: {data_transformation_artifacts}")
        
    def __convert_to_tf_data_and_apply_tokenizer(self, tokenizer, feature, label):
        # Function to tokenize and pad sequences
        def tokenize_and_pad(text, max_pad):
            text_lower = tf.strings.lower(text)
            byte_to_text = tf.compat.as_text(text_lower.numpy())
            sequences = tokenizer.texts_to_sequences([byte_to_text])
            padded = pad_sequences(sequences, maxlen=max_pad, padding='post')
            return padded[0]
        
        def tf_tokenize_and_pad(text, label, max_pad):
            label = tf.cast(label, tf.int32)
            text_tokenized = tf.py_function(tokenize_and_pad, inp=[text, max_pad], Tout=(tf.int32))
            text_tokenized.set_shape((max_pad, ))
            return text_tokenized, label

        try:
            logging.info(f"Converting data to tf.data.Dataset and applying tokenizer")
            tf_dataset = tf.data.Dataset.from_tensor_slices((feature, label))
            
            tf_dataset_tokenized = tf_dataset.map(
                map_func= lambda review, sentiment:
                    tf_tokenize_and_pad(
                        text=review,
                        label=sentiment,
                        max_pad=self.model_trainer_config.MAX_PAD
                    ),
                num_parallel_calls=tf.data.AUTOTUNE
            )
            tf_dataset_cached = tf_dataset_tokenized.cache()
            logging.info("Successfully tokenized and cached tf.data.Dataset")
            return tf_dataset_cached
        except Exception as e:
            logging.error(f"Error in __convert_to_tf_data_and_apply_tokenizer: {str(e)}", exc_info=True)
            raise CustomException(e, sys)
    
    def __tokenizing(self, feature):
        try:
            logging.info("Creating tokenizer and fitting on text data")
            tokenizer = Tokenizer(num_words=self.model_trainer_config.VOCAB_SIZE, oov_token=self.model_trainer_config.OOV_TOKEN)
            tokenizer.fit_on_texts(feature)
            return tokenizer
        except Exception as e:
            logging.error(f"Error in __tokenizing: {str(e)}", exc_info=True)
            raise CustomException(e, sys)
    
    def __preparing_data_training(self, data_path):
        try:
            logging.info(f"Preparing data for training from {data_path}")
            df = pd.read_csv(data_path)
            feature = df[FEATURE]
            label = df[LABEL]
            
            tokenizer = self.__tokenizing(feature)

            tf_data = self.__convert_to_tf_data_and_apply_tokenizer(tokenizer, feature, label)

            splitter = DatasetSplitter(
                batch_size=self.model_trainer_config.BATCH_SIZE, 
                train_split=self.model_trainer_config.TRAIN_SPLIT, 
                seed=self.model_trainer_config.SEED
            )

            tf_data_train, tf_data_valid = splitter.split_and_prepare(tf_data)
            logging.info("Data successfully split into training and validation sets")
            return tf_data_train, tf_data_valid, tokenizer
        except Exception as e:
            logging.error(f"Error in __preparing_data_training: {str(e)}", exc_info=True)
            raise CustomException(e, sys)
        
    def __callbacks(self):
        try:
            logging.info("Creating callbacks for model training")
            checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
                filepath=self.model_trainer_config.TRAINED_MODEL_PATH,  
                monitor=self.model_trainer_config.MONITOR, 
                save_best_only=self.model_trainer_config.SAVE_BEST_ONLY,  
                save_weights_only=self.model_trainer_config.SAVE_WEIGHTS_ONLY,
                mode=self.model_trainer_config.MODE_CHECKPOINT,
                verbose=self.model_trainer_config.VERBOSE
            )

            plateau_callback = tf.keras.callbacks.ReduceLROnPlateau(
                monitor=self.model_trainer_config.MONITOR, 
                factor=self.model_trainer_config.FACTOR,
                patience=self.model_trainer_config.PATIENCE_PLATEAU,
                verbose=self.model_trainer_config.VERBOSE,
                mode=self.model_trainer_config.MODE_PLATEAU,
                min_delta=self.model_trainer_config.MIN_DELTA,
                cooldown=self.model_trainer_config.COOLDOWN,
                min_lr=self.model_trainer_config.MIN_LR 
            )

            early_stopping = tf.keras.callbacks.EarlyStopping(
                monitor=self.model_trainer_config.MONITOR,
                patience=self.model_trainer_config.PATIENCE_EARLY_STOPPING,
                restore_best_weights=self.model_trainer_config.RESTORE_BEST_WEIGHTS,
                verbose=self.model_trainer_config.VERBOSE
            )
            logging.info("Callbacks successfully created")
            return [checkpoint_callback, plateau_callback, early_stopping]
        except Exception as e:
            logging.error(f"Error in __callbacks: {str(e)}", exc_info=True)
            raise CustomException(e, sys)

    def initiate_model_trainer(self) -> ModelTrainerArtifacts:
        logging.info("Started model training initiation process")
        try:
            tf_data_train, tf_data_valid, tokenizer_obj = self.__preparing_data_training(self.data_transformation_artifacts.transformed_data_file_path)
            logging.info("Data preparation completed")

            model = build_lstm_model(
                vocab_size=self.model_trainer_config.VOCAB_SIZE,
                embedding_dim=self.model_trainer_config.EMBEDDING_DIM,
            )

            model.compile(
                loss=self.model_trainer_config.LOSS,
                optimizer=self.model_trainer_config.OPTIMIZER,
                metrics=self.model_trainer_config.METRICS,
            )

            model.summary()

            logging.info("LSTM model successfully built")

            callbacks = self.__callbacks()

            os.makedirs(
                self.model_trainer_config.MODEL_TRAINER_ARTIFACTS_DIR,
                exist_ok=True
            )
            logging.info(f"Created model trainer artifacts directory: {self.model_trainer_config.MODEL_TRAINER_ARTIFACTS_DIR}")

            model.fit(
                tf_data_train,
                validation_data=tf_data_valid,
                epochs=self.model_trainer_config.EPOCHS,
                callbacks=callbacks
            )
            logging.info("Model training completed successfully")

            tf_data_valid.save(self.model_trainer_config.VALIDATION_DATA_PATH, compression="GZIP")
            logging.info(f"Data validation saved at {self.model_trainer_config.VALIDATION_DATA_PATH}")

            save_object(
                file_path=self.model_trainer_config.TOKENIZER_PATH,
                obj=tokenizer_obj
            )
            logging.info(f"Tokenizer object saved at {self.model_trainer_config.TOKENIZER_PATH}")

            model_trainer_artifacts = ModelTrainerArtifacts(
                trained_model_path=self.model_trainer_config.TRAINED_MODEL_PATH,
                tokenizer_path=self.model_trainer_config.TOKENIZER_PATH,
                validation_data_path=self.model_trainer_config.VALIDATION_DATA_PATH,
            )
            logging.info("ModelTrainerArtifacts created successfully")

            return model_trainer_artifacts
        except Exception as e:
            logging.error(f"Error in initiate_model_trainer: {str(e)}", exc_info=True)
            raise CustomException(e, sys)