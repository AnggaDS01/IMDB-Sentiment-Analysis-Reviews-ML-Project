from dataclasses import dataclass
from imbd_sentiment.constants import *

@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(
            os.getcwd(), 
            ARTIFACTS_DIR, 
            DATA_INGESTION_ARTIFACTS_DIR
        )

        self.SOURCE_URL = f"https://drive.google.com/uc?id={FILE_ID}"

        self.DATA_ARTIFACTS_PATH: str = os.path.join(
            self.DATA_INGESTION_ARTIFACTS_DIR,
            DATA_FILE_NAME
        )

        self.ZIP_FILE_DIR = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR)
        
        self.ZIP_FILE_PATH = os.path.join(
            self.DATA_INGESTION_ARTIFACTS_DIR,
            ZIP_FILE_NAME
        )

@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.DATA_TRANSFORMATION_ARTIFACTS_DIR: str = os.path.join(
            os.getcwd(),
            ARTIFACTS_DIR,
            DATA_TRANSFORMATION_ARTIFACTS_DIR
        )

        self.TRANSFORMED_FILE_PATH: str = os.path.join(
            self.DATA_TRANSFORMATION_ARTIFACTS_DIR,
            TRANSFORMED_FILE_NAME,
        )

        self.LABEL_TRANSFORMER_PATH: str = os.path.join(
            self.DATA_TRANSFORMATION_ARTIFACTS_DIR,
            LABEL_TRANSFORMER_NAME,
        )

@dataclass
class ModelTrainerConfig:
    def __init__(self):
        self.MODEL_TRAINER_ARTIFACTS_DIR: str = os.path.join(
            os.getcwd(),
            ARTIFACTS_DIR,
            MODEL_TRAINER_ARTIFACTS_DIR
        )

        self.TRAINED_MODEL_PATH: str = os.path.join(
            self.MODEL_TRAINER_ARTIFACTS_DIR,
            TRAINED_MODEL_NAME,
        )

        self.TOKENIZER_PATH: str = os.path.join(
            self.MODEL_TRAINER_ARTIFACTS_DIR,
            TOKENIZER,
        )

        self.VALIDATION_DATA_PATH: str = os.path.join(
            self.MODEL_TRAINER_ARTIFACTS_DIR,
            VALIDATION_DATA_NAME,
        )

        self.LOSS = LOSS
        self.OPTIMIZER = OPTIMIZER
        self.METRICS = METRICS
        self.OOV_TOKEN = OOV_TOKEN
        self.ACTIVATION_OUTPUT = ACTIVATION_OUTPUT
        self.VOCAB_SIZE = VOCAB_SIZE
        self.MAX_PAD = MAX_PAD
        self.SEED = SEED
        self.EPOCHS = EPOCHS
        self.BATCH_SIZE = BATCH_SIZE
        self.TRAIN_SPLIT = TRAIN_SPLIT
        self.EMBEDDING_DIM = EMBEDDING_DIM
        self.MONITOR = MONITOR
        self.SAVE_BEST_ONLY = SAVE_BEST_ONLY
        self.SAVE_WEIGHTS_ONLY = SAVE_WEIGHTS_ONLY
        self.MODE_CHECKPOINT = MODE_CHECKPOINT
        self.VERBOSE = VERBOSE
        self.FACTOR = FACTOR
        self.PATIENCE_PLATEAU = PATIENCE_PLATEAU
        self.MODE_PLATEAU = MODE_PLATEAU
        self.MIN_DELTA = MIN_DELTA
        self.COOLDOWN = COOLDOWN
        self.MIN_LR = MIN_LR
        self.PATIENCE_EARLY_STOPPING = PATIENCE_EARLY_STOPPING
        self.RESTORE_BEST_WEIGHTS = RESTORE_BEST_WEIGHTS