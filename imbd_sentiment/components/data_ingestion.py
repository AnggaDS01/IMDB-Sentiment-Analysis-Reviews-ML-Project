from imbd_sentiment.logger import logging
from imbd_sentiment.exception import CustomException
from imbd_sentiment.entity.config_entity import DataIngestionConfig
from imbd_sentiment.entity.artifact_entity import DataIngestionArtifacts

from zipfile import ZipFile
import os
import sys
import gdown

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    def get_data_from_gdrive(self) -> None:
        logging.info("Entered the get_data_from_gdrive method of Data ingestion class")
        try:
            
            os.makedirs(
                self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR, 
                exist_ok=True
            )

            gdown.download(
                self.data_ingestion_config.SOURCE_URL,
                self.data_ingestion_config.ZIP_FILE_PATH,
            )

            logging.info("Exited the get_data_from_gcdrive method of Data ingestion class")
        except Exception as e:
            raise CustomException(e, sys)

    def extract_zip_file(self):
        logging.info("Entered the extract_zip_file method of Data ingestion class")
        try: 
            with ZipFile(self.data_ingestion_config.ZIP_FILE_PATH, 'r') as zip_ref:
                zip_ref.extractall(self.data_ingestion_config.ZIP_FILE_DIR)

            logging.info("Exited the extract_zip_file method of Data ingestion class")

            return self.data_ingestion_config.DATA_ARTIFACTS_DIR

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the initiate_data_ingestion method of Data ingestion class")
        try:

            self.get_data_from_gdrive()
            logging.info("Fetched the data from gdrive")
            imdb_data_file_path = self.extract_zip_file()
            logging.info("Unzipped file")

            data_ingestion_artifacts = DataIngestionArtifacts(
                raw_data_file_path = imdb_data_file_path
            )

            logging.info("Exited the initiate_data_ingestion method of Data ingestion class")

            logging.info(f"Data ingestion artifact: {data_ingestion_artifacts}")

            return data_ingestion_artifacts

        except Exception as e:
            raise CustomException(e, sys)