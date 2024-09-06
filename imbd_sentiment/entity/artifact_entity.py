from dataclasses import dataclass

# Data ingestion artifacts
@dataclass
class DataIngestionArtifacts:
    raw_data_file_path: str

@dataclass
class DataTransformationArtifacts:
    label_transformer_file_path: str
    transformed_data_file_path: str