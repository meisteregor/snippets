import logging
import config
import os

formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logfile = os.path.dirname(os.path.abspath(__file__)) + "/" + config.LOG_FILE
file_handler = logging.FileHandler(logfile)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(console)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
