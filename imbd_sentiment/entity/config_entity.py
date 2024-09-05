from dataclasses import dataclass
from imbd_sentiment.constants import *

@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.SOURCE_URL = f"https://drive.google.com/uc?id={FILE_ID}"
        self.DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(
            os.getcwd(), 
            ARTIFACTS_DIR, 
            DATA_INGESTION_ARTIFACTS_DIR
        )

        self.DATA_ARTIFACTS_DIR: str = os.path.join(
            self.DATA_INGESTION_ARTIFACTS_DIR,
            DATA_INGESTION_IMBD_DATA_DIR
        )

        self.ZIP_FILE_DIR = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR)
        self.ZIP_FILE_PATH = os.path.join(
            self.DATA_INGESTION_ARTIFACTS_DIR,
            ZIP_FILE_NAME
        )

