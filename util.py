from time import time

def secs_to_wait(reset):
    """Return seconds to wait to reset.

    reset -- UTC epoch seconds. This is converted into an integer value
    """
    # floor  time() to get a conservative result.
    now = int(time() - 1)
    return max(int(reset) - now, 0)
