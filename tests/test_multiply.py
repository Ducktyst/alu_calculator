from mathematic.arithmetic import muliply, muliply2


def test_multiply():
    res = muliply(0, 0)
    assert res == 0, f"Получено {res}"

    res = muliply(0, 1)
    assert res == 0, f"Получено {res}"

    res = muliply(1, 0)
    assert res == 0, f"Получено {res}"

    res = muliply(1, 1)
    assert res == 1, f"Получено {res}"


def test_multiply1():
    assert muliply(10111, 101) == 1110011

def test_multiply2():
    res = muliply2(0, 0)
    assert muliply2(0, 0) == ['0']*8, f"Получено {res}"

    res = muliply2(0, 1)
    assert muliply2(0, 1) == ['0']*8, f"Получено {res}"

    res = muliply2(1, 0)
    assert muliply2(1, 0) == ['0']*8, f"Получено {res}"

    res = muliply2(1, 1)
    assert  muliply2(1, 1) == ['0']*7 + ['1'], f"Получено {res}"
