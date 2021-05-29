from mathematic.arithmetic import division


def test_division():
    """
    Проверка деления двоичных числел
    """
    #
    assert (division(['0', '0', '0', '0', '1', '1', '1', '1'],
                     ['0', '0', '0', '0', '0', '1', '1', '0'], 8) ==
            ['0', '0', '0', '0', '0', '1', '0', '1'])


def test_division2():
    """
    Проверка деления двоичных числел
    """
    # 11 / 5
    res = division(list('1011'), list('0101'), 4)
    assert (res == list('0010')), f'Получено: {res}'


    # 10 / 5
    res = division(list('1010'), list('0101'), 4)
    assert (res == list('0010')), f'Получено: {res}'

    # 5 / 10
    res = division(list('00000101'), list('00001010'), 8)
    assert (res == list('0')), f'Получено: {res}'


def test_division_result_len():
    """ Проверка соответствия разрядности возвращаемого регистра"""

    # 10 / 5
    res = division(list('1010'), list('0101'), 4)
    assert (res == list('0010')), f'Получено: {res}'

    # 10 / 5
    res = division(list('00001010'), list('00000101'), 8)
    assert (res == list('00000010')), f'Получено: {res}'