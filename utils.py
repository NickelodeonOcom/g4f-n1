import time
import logging

# Simple logger setup
def setup_logger(name=__name__, level=logging.INFO):
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger

logger = setup_logger()

# Retry decorator for network or unstable calls
def retry(times, exceptions):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning(f'Attempt {attempt+1} failed: {e}')
                    time.sleep(2 ** attempt)
            raise Exception(f'Failed after {times} attempts')
        return wrapper
    return decorator
