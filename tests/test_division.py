from mathematic.arithmetic import division


def test_division():
    """
    Проверка деления двоичных числел
    """
    assert (division(['0', '0', '0', '0', '1', '1', '1', '1'],
                     ['0', '0', '0', '0', '0', '1', '1', '0'], 8) ==
            ['0', '0', '0', '0', '0', '1', '0', '1'])


def test_division2():
    """
    Проверка деления двоичных числел
    """
    # 11 / 2
    res = division(list('1011'), list('0101'), 4)
    assert (res == list('0010')), f'Получено: {res}'

    # 10 / 2
    res = division(list('1010'), list('0101'), 4)
    assert (res == list('0010')), f'Получено: {res}'

    res = division(list('00001010'), list('00000101'), 8)
    assert (res == list('00000010')), f'Получено: {res}'
