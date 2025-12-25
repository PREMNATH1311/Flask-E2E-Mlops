from src.FlaskMlops import logger
from src.FlaskMlops.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.FlaskMlops.pipeline.data_validation_pipeline import DataValidationTraniningPipeline
from src.FlaskMlops.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.FlaskMlops.pipeline.model_trainer_pipeline import ModelTrainerPipeline


STAGE_NAME= "Data Ingestion stage"

try:
    logger.info(f">>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<")
    data_ingestion=DataIngestionPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<<<<\n \n ")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Data Validation stage"
try:
    logger.info(f">>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<")
    data_validation=DataValidationTraniningPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<<<<\n \n ")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Data Transformation stage"
try:
    logger.info(f">>>>>>>>>>>>>>>> stage '{STAGE_NAME}'  started <<<<<<<<<<<<<<<<<")
    data_transformation=DataTransformationPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<<<<\n \n ")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Trainer stage"

try:
    logger.info(f">>>>>>>>>>>>>>>> stage '{STAGE_NAME}' started <<<<<<<<<<<<<<<<<")
    model_trainer=ModelTrainerPipeline()
    model_trainer.initiate_model_trainer()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<<<<\n \n ")
except Exception as e:
    logger.exception(e)
    raise e