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
        logging.info(f"DataIngestion initialized with config: {data_ingestion_config}")

    def __get_data_from_gdrive(self) -> None:
        logging.info("Entered the __get_data_from_gdrive method of DataIngestion class")
        try:
            logging.info(f"Creating directory: {self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR}")
            os.makedirs(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR, exist_ok=True)
            logging.info(f"Directory created or already exists: {self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR}")

            logging.info(f"Downloading file from Google Drive URL: {self.data_ingestion_config.SOURCE_URL}")
            gdown.download(
                self.data_ingestion_config.SOURCE_URL,
                self.data_ingestion_config.ZIP_FILE_PATH,
                quiet=False
            )
            logging.info(f"File downloaded successfully to: {self.data_ingestion_config.ZIP_FILE_PATH}")
            logging.info("Exited the __get_data_from_gdrive method of DataIngestion class")

        except Exception as e:
            logging.error("Error occurred in __get_data_from_gdrive", exc_info=True)
            raise CustomException(e, sys)

    def __extract_zip_file(self):
        logging.info("Entered the __extract_zip_file method of DataIngestion class")
        try:
            logging.info(f"Extracting ZIP file: {self.data_ingestion_config.ZIP_FILE_PATH}")
            with ZipFile(self.data_ingestion_config.ZIP_FILE_PATH, 'r') as zip_ref:
                zip_ref.extractall(self.data_ingestion_config.ZIP_FILE_DIR)
            logging.info(f"File extracted to: {self.data_ingestion_config.ZIP_FILE_DIR}")
            logging.info("Exited the __extract_zip_file method of DataIngestion class")

            # return self.data_ingestion_config.DATA_ARTIFACTS_PATH

        except Exception as e:
            logging.error("Error occurred in __extract_zip_file", exc_info=True)
            raise CustomException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the initiate_data_ingestion method of DataIngestion class")
        try:
            logging.info("Starting data ingestion process")
            self.__get_data_from_gdrive()
            logging.info("Data successfully fetched from Google Drive")

            self.__extract_zip_file()
            logging.info("ZIP file successfully extracted")

            data_ingestion_artifact_obj = DataIngestionArtifacts(
                raw_data_file_path=self.data_ingestion_config.DATA_ARTIFACTS_PATH
            )
            logging.info(f"DataIngestionArtifacts created: {data_ingestion_artifact_obj}")

            logging.info("Exited the initiate_data_ingestion method of DataIngestion class")
            return data_ingestion_artifact_obj

        except Exception as e:
            logging.error("Error occurred in initiate_data_ingestion", exc_info=True)
            raise CustomException(e, sys)