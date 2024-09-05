import os
from datetime import datetime

# Common constants
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)
FILE_ID = '1wDV_Uf9RHuduQJi_tdiY7pcGly6ISk8r'
ZIP_FILE_NAME = 'IMDB Dataset.zip'
LABEL = 'sentiment'
TWEET = 'review'

# Data ingestion constants
DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_INGESTION_IMBD_DATA_DIR = "IMDB Dataset.csv"
