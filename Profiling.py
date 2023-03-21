import time
from time import sleep
import datetime
from functools import wraps
import logging

logging.basicConfig(filename="Profiling file",
                    format='%(asctime)s - %(message)s', level=logging.INFO)


def profile(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        t = datetime.datetime.now()
        my_function = function(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f'{t} - {function.__name__}, {execution_time}')
        return my_function

    return wrapper


@profile
def foo(x):
    sleep(2)
    return x ** 2


print(foo(2))
sleep(60)
print(foo(42))

