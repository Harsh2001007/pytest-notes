import logging
import inspect

class BaseContainerLogs:
    
    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        fileName = logging.FileHandler('logfile.log')

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileName.setFormatter(formatter)

        logger.addHandler(fileName)

        logger.setLevel(logging.INFO)
        
        
        
        


        # logger.debug("A debug statement is returned")
        # logger.info(" Information statement")
        # logger.warning("Test is in warning mode")
        # logger.error("A major error is occured")
        # logger.critical("Critical situation")

        return logger