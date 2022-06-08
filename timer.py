from timeit import default_timer as timer
import math
import time


def measure_time(func):
    def inner(*args, **kwargs):
        start = timer()

        func(*args, **kwargs)

        end = timer()

        print(f'Function {func.__name__} took {round(end-start, 5)} for execution')
    return inner


@measure_time
def factorial(num):
    time.sleep(3)
    print(math.factorial(num))


factorial(100)

