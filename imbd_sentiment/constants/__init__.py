import os
from datetime import datetime

# Common constants
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)
BUCKET_NAME = 'hate-speech2024'
ZIP_FILE_NAME = 'dataset.zip'
LABEL = 'sentiment'
TWEET = 'review'