from datetime import datetime
import logging
from functools import wraps

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(name)s %(levelname)s %(message)s")


def log(level):
    def decorator(func_or_class):
        if isinstance(func_or_class, type):
            @wraps(func_or_class)
            def wrapper(*args, **kwargs):
                instance = func_or_class(*args, **kwargs)
                logger = logging.getLogger(func_or_class.__name__)
                logger.log(level, f'Created {func_or_class.__name__} instance')
                return instance
            return wrapper
        else:
            @wraps(func_or_class)
            def wrapper(*args, **kwargs):
                start_time = datetime.now()
                logger = logging.getLogger(func_or_class.__name__)
                logger.log(level, f'Started {func_or_class.__name__} with args: {args}, kwargs: {kwargs}')
                result = func_or_class(*args, **kwargs)
                end_time = datetime.now()
                duration = end_time - start_time
                logger.log(level, f'Finished {func_or_class.__name__}. Duration: {duration}. Returned: {result}')
                return result
            return wrapper
    return decorator


@log(logging.DEBUG)
def add(x, y):
    return x+y


if __name__ == "__main__":
    add(2, 3)
