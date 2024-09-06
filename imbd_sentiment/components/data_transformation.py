from imbd_sentiment.logger import logging
from imbd_sentiment.exception import CustomException
from imbd_sentiment.entity.config_entity import DataTransformationConfig
from imbd_sentiment.entity.artifact_entity import (
    DataTransformationArtifacts, 
    DataIngestionArtifacts
)
from imbd_sentiment.constants import (
    LABEL, 
    FEATURE, 
)
from imbd_sentiment.utils import save_object

from sklearn.preprocessing import LabelBinarizer
from tqdm import tqdm

import sys
import re
import os
import pandas as pd

tqdm.pandas()

class DataTransformation:
    def __init__(self, data_transformation_config_obj: DataTransformationConfig, data_ingestion_artifacts_obj: DataIngestionArtifacts):
        self.data_transformation_config_obj = data_transformation_config_obj
        self.data_ingestion_artifacts_obj = data_ingestion_artifacts_obj
        logging.info(f"Initialized DataTransformation with config: {data_transformation_config_obj} and ingestion artifacts: {data_ingestion_artifacts_obj}")
    
    def __label_transformation(self, data):
        try:
            logging.info("Starting label transformation.")
            lb = LabelBinarizer()
            label_transformer_obj = lb.fit(data[LABEL])
            logging.info("Label transformation completed.")
            return label_transformer_obj
        except Exception as e:
            logging.error("Error in label transformation", exc_info=True)
            raise CustomException(e, sys)

    def __clean_reviews_transformation(self, review):
        try:
            # Menghapus tag HTML menggunakan regex
            review = re.sub(r'<.*?>', '', review.lower())

            # Menghapus URL/link
            review = re.sub(r'http\S+|www\S+|https\S+', '', review)

            # Mengganti semua kata dengan tanda hubung menjadi versi tanpa tanda hubung
            review = re.sub(r'(\w+)(-\w+)+', lambda x: x.group(0).replace('-', ' '), review)

            # Menghapus karakter khusus selain huruf, angka, dan spasi
            review = re.sub(r'[^a-zA-Z0-9\s]', '', review)

            # Menghapus spasi yang berlebihan
            review = re.sub(r'\s+', ' ', review).strip()

            return review
        except Exception as e:
            logging.error("Error in review cleaning", exc_info=True)
            raise CustomException(e, sys)

    def initiate_data_transformation(self) -> DataTransformationArtifacts:
        try:
            logging.info(f"Loading raw data from {self.data_ingestion_artifacts_obj.raw_data_file_path}")
            df = pd.read_csv(self.data_ingestion_artifacts_obj.raw_data_file_path)
            logging.info(f"Data loaded successfully. Shape: {df.shape}")
            
            logging.info("Starting label transformation process.")
            label_transformer_obj = self.__label_transformation(df)

            logging.info(f"Review sample: {df[FEATURE][0]}...")  # Log a preview of the review
            logging.info("Applying review cleaning transformation.")
            df[FEATURE] = df[FEATURE].progress_apply(self.__clean_reviews_transformation)
            logging.info(f"Cleaning review: {df[FEATURE][0]}...")  # Log a preview of the review
            
            logging.info("Transforming labels using label transformer.")
            df[LABEL] = label_transformer_obj.transform(df[LABEL])

            logging.info(f"Creating directory for transformation artifacts: {self.data_transformation_config_obj.DATA_TRANSFORMATION_ARTIFACTS_DIR}")
            os.makedirs(
                self.data_transformation_config_obj.DATA_TRANSFORMATION_ARTIFACTS_DIR,
                exist_ok=True
            )

            logging.info(f"Saving transformed data to {self.data_transformation_config_obj.TRANSFORMED_FILE_PATH}")
            df.to_csv(
                self.data_transformation_config_obj.TRANSFORMED_FILE_PATH,
                index=False,
                header=True
            )

            logging.info(f"Saving label transformer object to {self.data_transformation_config_obj.LABEL_TRANSFORMER_PATH}")
            save_object(
                file_path=self.data_transformation_config_obj.LABEL_TRANSFORMER_PATH,
                obj=label_transformer_obj
            )

            data_transformation_artifact_obj = DataTransformationArtifacts(
                label_transformer_file_path=self.data_transformation_config_obj.LABEL_TRANSFORMER_PATH,
                transformed_data_file_path=self.data_transformation_config_obj.TRANSFORMED_FILE_PATH
            )

            logging.info("Data transformation process completed successfully.")
            return data_transformation_artifact_obj

        except Exception as e:
            logging.error("Error during data transformation process", exc_info=True)
            raise CustomException(e, sys)      
