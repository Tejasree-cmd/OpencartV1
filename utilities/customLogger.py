import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s: %(levelname)s : %(message)s' ,datefmt='%m%d%Y %I:%M:%S %p',
                            handlers=[
                                logging.StreamHandler(),
                                logging.FileHandler('.\\logs\\automation.log')

                            ],force=True )
        #
        logger = logging.getLogger(__name__)

        logger.setLevel(logging.DEBUG)
        return logger