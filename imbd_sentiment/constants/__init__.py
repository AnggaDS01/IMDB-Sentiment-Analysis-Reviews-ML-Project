import os
from datetime import datetime

# Common constants
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)
FILE_ID = '1wDV_Uf9RHuduQJi_tdiY7pcGly6ISk8r'
ZIP_FILE_NAME = 'IMDB Dataset.zip'
LABEL = 'sentiment'
FEATURE = 'review'

# Data ingestion constants
DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_FILE_NAME = "IMDB Dataset.csv"

# Data Transformation constants
DATA_TRANSFORMATION_ARTIFACTS_DIR = "DataTransformationrtifacts"
TRANSFORMED_FILE_NAME = "imdb_reviews_final.csv"
LABEL_TRANSFORMER_NAME = "label_transformer.pkl"

# Model Training Constants 
MODEL_TRAINER_ARTIFACTS_DIR = "ModelTrainingArtifacts"
TRAINED_MODEL_NAME = "imdb_lstm_model.keras"
TOKENIZER = "tokenizer.pickle"
VALIDATION_DATA_NAME = "imbd_data_valid.tfrecord"
LOSS = "binary_crossentropy"
OPTIMIZER = "adam"
METRICS = ["accuracy", "Precision", "Recall"]
OOV_TOKEN = "<UNK>"
ACTIVATION_OUTPUT = "sigmoid"
VOCAB_SIZE = 10000
MAX_PAD = 228
SEED = 42
EPOCHS = 1
BATCH_SIZE = 64
TRAIN_SPLIT = 0.8
EMBEDDING_DIM = 64

# Checkpoint Callback Constants
MONITOR = "val_loss"
SAVE_BEST_ONLY = True
SAVE_WEIGHTS_ONLY = False
MODE_CHECKPOINT = "min"
VERBOSE = 1

# Plateau Callback Constants
FACTOR = 0.5
PATIENCE_PLATEAU = 20
MODE_PLATEAU = "auto"
MIN_DELTA = 0.001
COOLDOWN = 0
MIN_LR = 0

# Early Stopping Callback Constants
PATIENCE_EARLY_STOPPING = 25
RESTORE_BEST_WEIGHTS = True