from custom_logger import logger


def undef_behaviour_catcher(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logger.critical(e)
            raise

    return inner
