from imbd_sentiment.components.data_ingestion import DataIngestion
from imbd_sentiment.entity.config_entity import DataIngestionConfig

test = DataIngestionConfig()

get_data = DataIngestion(test)
get_data.get_data_from_gdrive()