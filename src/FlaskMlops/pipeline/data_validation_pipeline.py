from src.FlaskMlops.config.configuration import ConfigurationManager
from src.FlaskMlops.components.data_validation import Datavalidation
from src.FlaskMlops import logger



STAGE_NAME= "Data Validation stage"

class DataValidationTraniningPipeline:
    def __init__(self):
        pass
    
    def initiate_data_validation(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=Datavalidation(config=data_validation_config)
        data_validation.validate_all_columns()
    
if __name__== "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        obj=DataValidationTraniningPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<< \n \n ")
        
    except Exception as e:
        logger.exception(e)
        raise e

