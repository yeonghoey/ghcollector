# -*- coding: utf-8 -*-

from time import time
from ghcollector.util import secs_to_wait

def test_secs_to_wait():
    def test(dt):
        ret = secs_to_wait(time() + dt)
        if dt < 0:
            assert ret == 0
        else:
            assert ret >= dt and ret <= dt + 1

    test(10)
    test(1)
    test(0)
    test(-1)
    test(10)

