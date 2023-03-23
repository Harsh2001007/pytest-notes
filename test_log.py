import logging

def test_logCode():

    logger = logging.getLogger(__name__)

    logFile = logging.FileHandler("log2.log")
    logFormat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    logFile.setFormatter(logFormat)

    logger.addHandler(logFile)
    logger.setLevel(logging.DEBUG)



    logger.debug("debug required")
    logger.info("information")
    logger.warning("warnigns are appearing")
    logger.error("error detected")
    logger.critical("critical issue")