from src.FlaskMlops.config.configuration import ConfigurationManager
from src.FlaskMlops.components.model_evaluation import ModelEvaluation
from src.FlaskMlops import logger




class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def initiate_model_evaluation(self):
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation=ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()        
