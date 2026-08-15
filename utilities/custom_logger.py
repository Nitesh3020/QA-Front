import inspect
import logging

def customLogger(loglevel=logging.DEBUG):
    loggerName = inspect.stack()[1][3]
    logger= logging.getLogger(loggerName)

    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(loglevel)

    formatter =logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger