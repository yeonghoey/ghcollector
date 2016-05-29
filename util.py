from time import time

def secs_to_wait(reset):
    """Return seconds to wait to reset.

    reset -- UTC epoch seconds. This is converted into an integer value
    """
    # floor seconds in double to get a conservative result.
    reset = int(reset)
    now = int(time() - 1)
    return max(reset - now, 0)
