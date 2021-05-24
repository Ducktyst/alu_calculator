from mathematic.arithmetic import summa
from tests.utils import asssert_equal


def test_sum():
    """ Проверка примитивных случаев"""
    asssert_equal(['0', '0', '0', '0', '0', '0', '0', '0'], summa, ['0'], ['0'])
    assert summa(['0'], ['1']) == ['0', '0', '0', '0', '0', '0', '0', '1'], f"Got: {summa(['0'], ['1'])}"
    assert summa(['1'], ['0']) == ['0', '0', '0', '0', '0', '0', '0', '1']
    assert summa(['1'], ['1']) == ['0', '0', '0', '0', '0', '0', '1', '0']

    assert summa(['1', '0', '0', '0', '0', '0', '0', '0'], ['0']) == ['1', '0', '0', '0', '0', '0', '0', '0']


def test_sum1():
    """ Проверка сложения чисел разной длины"""
    num1 = list(str(101))
    num2 = list(str(100101))

    res1 = summa(num1, num2)
    assert res1 == ['0', '0', '1', '0', '1', '0', '1', '0']

def test_sum2():
    """ Проверка базового случая сложения"""
    num1 = list(str(100101))
    num2 = list(str(101))

    res = summa(num1, num2)
    assert res == ['0', '0', '1', '0', '1', '0', '1', '0']


def test_sum3():
    """
    Проверка переходов в следующий разряд
    """
    num1 = list(str(111))
    num2 = list(str(111))

    res = summa(num1, num2)
    assert res == ['0', '0', '0', '0', '1', '1', '1', '0']
