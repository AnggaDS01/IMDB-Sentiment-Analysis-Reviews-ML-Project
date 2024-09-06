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