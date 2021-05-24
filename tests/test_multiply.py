from mathematic.arithmetic import muliply


def test_multiply():
    assert muliply(0, 0) == 0
    assert muliply(0, 1) == 0
    assert muliply(1, 0) == 0
    assert muliply(1, 1) == 1

def test_multiply1():
    assert muliply(10111, 101) == 1110011
