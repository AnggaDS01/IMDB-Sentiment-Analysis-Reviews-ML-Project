from imbd_sentiment.pipeline.train_pipeline import TrainPipeline

obj = TrainPipeline()
data_ingestion_artifacts = obj.run_pipeline()
print(data_ingestion_artifacts)