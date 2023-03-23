import logging


def test_logging():
    logger = logging.getLogger(__name__)
    fileName = logging.FileHandler('logfile.log')

    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileName.setFormatter(formatter)

    logger.addHandler(fileName)

    logger.setLevel(logging.INFO)



    logger.debug("A debug statement is returned")
    logger.info(" Information statement")
    logger.warning("Test is in warning mode")
    logger.error("A major error is occured")
    logger.critical("Critical situation")
