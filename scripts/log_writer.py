"""This script writes log messages regarding the file it is called upon!!!"""
import logging

class log:
    "log class"

    def __init__(self, file_name: str, basic_level = logging.INFO):
        """Constructor: upon call initializes the logger class with the filename and log level"""
        
        logger = logging.getLogger(__name__)

        #set log level to INFO
        logger.setLevel(basic_level)

        file_handler = logging.FileHandler(f"../logs/{file_name}")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s: %(name)s: %(module)s: %(funcName)s: %(message)s")

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        self.logger = logger

    def get_app_logger(self) -> logging.log:
        return self.logger