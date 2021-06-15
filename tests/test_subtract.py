# import pytest

from mathematic.arithmetic import subtract_as_ints, subtract_using_additional_code
from tests.utils import asssert_equal


def test_minus():
    """
    Проверка вычитания базовых случаев
    """
    assert subtract_as_ints(0, 0) == 0
    assert subtract_as_ints(1, 0) == 1
    assert subtract_as_ints(1, 1) == 0
    assert subtract_as_ints(10, 1) == 1


def test_subtraction():
    """
    Тест вычитания
    """
    # 0 - 0
    expected = ['0', '0', '0', '0', '0', '0', '0', '0']
    asssert_equal(expected, subtract_using_additional_code, ['0'], ['0'])

    # 1 - 0
    expected = ['0', '0', '0', '0', '0', '0', '0', '1']
    asssert_equal(expected, subtract_using_additional_code, ['1'], ['0'])

    # 10 - 0
    expected = ['0', '0', '0', '0', '0', '0', '1', '0']
    asssert_equal(expected, subtract_using_additional_code, ['1', '0'], ['0'])

    # 10 - 01
    expected = ['0', '0', '0', '0', '0', '0', '1', '1']
    asssert_equal(expected, subtract_using_additional_code, ['1', '0'], ['1'])


def test_subtract():
    """
    Проверка вычитания
    """
    assert subtract_as_ints(1110, 101) == 1001


# def test_minus_a_lt_b():
#     """
#     Проверка случаея, когда уменьшаемое больше вычитаемого
#     """
#     pytest.raises(AssertionError, subtract_as_ints, 1, 1000)


def test_subtraend():
    """
    Проверка вычитания с использованем дополнительных кодов
    """
    expected = ['0', '0', '0', '0', '0', '0', '0', '0']
    asssert_equal(expected, subtract_using_additional_code, ['0'], ['0'])

    expected = ['0', '0', '0', '0', '0', '0', '0', '1']
    asssert_equal(expected, subtract_using_additional_code, *(['1'], ['0']))
    # asssert_equal('10000000', subtract_with_additional_code,'1', '1')
    # asssert_equal('00000001', subtract_with_additional_code,'10', '1')
    # asssert_equal('00001001', subtract_with_additional_code,'1110', '101')
