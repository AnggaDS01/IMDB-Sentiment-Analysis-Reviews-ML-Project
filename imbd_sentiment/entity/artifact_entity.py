from dataclasses import dataclass

# Data ingestion artifacts
@dataclass
class DataIngestionArtifacts:
    raw_data_file_path: str

@dataclass
class DataTransformationArtifacts:
    label_transformer_file_path: str
    transformed_data_file_path: str

@dataclass
class ModelTrainerArtifacts:
    trained_model_path: str
    tokenizer_path: str
    validation_data_path: str