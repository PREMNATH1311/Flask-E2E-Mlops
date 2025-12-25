from src.FlaskMlops.config.configuration import ConfigurationManager
from src.FlaskMlops.components.model_trainer import ModelTrainer
from src.FlaskMlops import logger




class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def initiate_model_trainer(self):
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer_config=ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
        
