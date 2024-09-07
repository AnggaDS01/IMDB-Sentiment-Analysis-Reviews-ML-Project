from imbd_sentiment.logger import logging
from imbd_sentiment.exception import CustomException

from imbd_sentiment.components.data_ingestion import DataIngestion
from imbd_sentiment.components.data_transformation import DataTransformation
from imbd_sentiment.components.model_trainer import ModelTrainer

from imbd_sentiment.entity.config_entity import (
    DataIngestionConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)
from imbd_sentiment.entity.artifact_entity import (
    DataIngestionArtifacts,
    DataTransformationArtifacts,
    ModelTrainerArtifacts
)

import sys

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()
        self.model_trainer_config = ModelTrainerConfig()

    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logging.info("Getting the data from Gdrive Storage")
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)

            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from Gdrive Storage")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifacts

        except Exception as e:
            raise CustomException(e, sys)
        
    def start_data_transformation(self, data_ingestion_artifacts = DataIngestionArtifacts) -> DataTransformationArtifacts:
        logging.info("Entered the start_data_transformation method of TrainPipeline class")
        try:
            data_transformation = DataTransformation(
                data_transformation_config_obj = self.data_transformation_config,
                data_ingestion_artifacts_obj = data_ingestion_artifacts,
            )

            data_transformation_artifacts = data_transformation.initiate_data_transformation()
            
            logging.info("Exited the start_data_transformation method of TrainPipeline class")
            return data_transformation_artifacts

        except Exception as e:
            raise CustomException(e, sys)

    def start_model_trainer(self, data_transformation_artifacts: DataTransformationArtifacts) -> ModelTrainerArtifacts:
        logging.info("Entered the start_model_trainer method of TrainPipeline class")
        try:
            model_trainer = ModelTrainer(
                model_trainer_config=self.model_trainer_config,
                data_transformation_artifacts=data_transformation_artifacts
            )
            model_trainer_artifacts = model_trainer.initiate_model_trainer()
            logging.info("Exited the start_model_trainer method of TrainPipeline class")
            return model_trainer_artifacts
        except Exception as e:
            raise CustomException(e, sys)
        
    def run_pipeline(self):
        logging.info("Entered the run_pipeline method of TrainPipeline class")
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            data_transformation_artifacts = self.start_data_transformation(
                data_ingestion_artifacts=data_ingestion_artifacts
            )

            model_trainer_artifacts = self.start_model_trainer(
                data_transformation_artifacts=data_transformation_artifacts
            )


            logging.info("Exited the run_pipeline method of TrainPipeline class") 
            return model_trainer_artifacts
        except Exception as e:
            raise CustomException(e, sys)