from loguru import logger
import os
import urllib3

# minimal
def set_logger():
    logfile = os.path.dirname(os.path.abspath(__file__)) + "/" + cons.LOGFILE
    logger.add(logfile, format="{time} {level} {message}", level="DEBUG", rotation="1 year",
               compression="zip")

# extended
def setup_logger():
    TIMESTAMP_STR = '<green>{time:YYYY-MM-DD HH:mm:ss}</green>'
    LOG_FORMAT_MINIMAL = "[<level>{level: <8}</level>] <level>{message}</level>"
    LOG_FORMAT_SCREEN = LOG_FORMAT_MINIMAL
    LOG_FORMAT_FILE = TIMESTAMP_STR + " " + LOG_FORMAT_MINIMAL
    LOG_FILE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/" + 'logs/' + os.path.basename(__file__).replace('.py', '.log')
    LOG_CONFIG = {
        "handlers": [
            {"sink": sys.stdout, "format": LOG_FORMAT_SCREEN, "level": "WARNING"},
            {"sink": LOG_FILE, "format": LOG_FORMAT_FILE, "level": "DEBUG", "rotation": "250 MB", "retention": "5 days", "compression": "zip"},
        ],
    }
  
    logger.configure(**LOG_CONFIG)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    urllib3.disable_warnings(urllib3.exceptions.SSLError)
    urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)
    logger.enable("alerts_api")
