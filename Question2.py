import time
import functools

def decorator(fun):
    @functools.wraps(fun)
    def timer(*args, **keyargs):
        original = time.time()
        value = fun(*args, **keyargs)
        end = time.time()
        run = end - original
        print(f"Finished {fun.__name__!r} in {run:.4f} secs")
        return value
    return timer