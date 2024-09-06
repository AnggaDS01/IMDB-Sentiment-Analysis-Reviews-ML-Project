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