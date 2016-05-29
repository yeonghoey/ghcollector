from time import time
from util import secs_to_wait

def test_secs_to_wait():
    secs_to_wait_from_now_by(10)
    secs_to_wait_from_now_by(1)
    secs_to_wait_from_now_by(0)
    secs_to_wait_from_now_by(-1)
    secs_to_wait_from_now_by(10)

def secs_to_wait_from_now_by(dt):
    ret = secs_to_wait(time() + dt)
    if dt < 0:
        assert ret == 0
    else:
        assert ret >= dt and ret <= dt + 1
