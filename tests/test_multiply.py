from mathematic.arithmetic import muliply

def test_multiply2():
    res = muliply(list('0'), list('0'), 16)
    assert res, f"Получено {res}"

    res = muliply(list('0'), list('1'), 16)
    assert res == ['0'] * 8, f"Получено {res}"

    res = muliply(list('1'), list('0'), 16)
    assert res == ['0'] * 8, f"Получено {res}"

    res = muliply(list('1'), list('1'), 16)
    assert res == list('00000001'), f"Получено {res}"

    res = muliply(list('11110'), list('10001'), 16)
    assert res == list('01110011'), f"Получено {res}"
