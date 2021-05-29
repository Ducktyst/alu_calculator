from typing import List

SIGN = 0  # индекс знакового разряда


def invert_sign(number: List[str]):
    return convert_to_additoinal_code(number[:], force=True)


def convert_to_additoinal_code(number: List[str], bits: int = 8, force=False) -> \
        List[str]:
    """ Преобразование числа из прямого в дополнителньый код.

    force - флаг принудельного преобзоавания для положительных чисел
    """
    ones_complement = number[:]

    # Дополнительный код положительного числа совпадает с прямым кодом.
    if ones_complement[0] == '0' and not force:
        return ones_complement

    if len(ones_complement) > bits:
        raise ValueError("Разрядность числа превышает максимальное число бит")

    ones_complement = ['0'] * (len(ones_complement) - bits) + ones_complement

    # Для отрицательного числа все цифры числа заменяются на противоположные (1 на 0, 0 на 1),
    for i in range(len(ones_complement)):
        if ones_complement[i] == '0':
            ones_complement[i] = '1'
        elif ones_complement[i] == '1':
            ones_complement[i] = '0'
        else:
            raise ValueError("Число должно быть в двоичной системе счисления")

    tmp_bits = len(ones_complement)
    additional_code = summa(ones_complement, ['0'] * (tmp_bits - 1) + ['1'],
                            tmp_bits)

    if len(additional_code) != bits:
        raise Exception("")

    return additional_code


def summa(num1: List[str], num2: List[str], bits=8) -> List[str]:
    """ Сложение чисел в двочиной системе счисления. """
    # num1 = ''.join(num1)
    # num2 = ''.join(num2)

    if len(num1) > bits or len(num2) > bits:
        raise Exception(f"{num1} {num2}")

    # уравнять числа по длине
    if len(num1) < bits:
        len_diff = bits - len(num1)
        num1 = (['0'] * len_diff) + num1

    if len(num2) < bits:
        len_diff = bits - len(num2)
        num2 = (['0'] * len_diff) + num2

    additional = False  # флаг переноса разряда
    result = ''
    for rank in range(1, bits + 1):
        bit1 = num1[-rank]
        bit2 = num2[-rank]

        if bit1 == '0' and bit2 == '0':
            if additional:
                result = '1' + result
                additional = False
            elif not additional:
                result = '0' + result
        elif (bit1 == '0' and bit2 == '1') or (bit1 == '1' and bit2 == '0'):
            if additional:
                result = '0' + result
                additional = True
            elif not additional:
                result = '1' + result
        elif bit1 == '1' and bit2 == '1':
            if additional:
                result = '1' + result
            elif not additional:
                result = '0' + result
            additional = True

    return list(result)


def subtract_as_ints(minuend: int, subtrahend: int) -> int:
    """ Вычитание.

    Вычитание столбиком
    """
    num1_str = str(minuend)
    num2_str = str(subtrahend)
    assert len(num1_str) >= len(num2_str), \
        'Допускается вычитание только в оложительных числах'

    take_rank = False
    difference = list(num1_str)
    for i in range(1, len(num1_str) + 1):
        minuend_number = num1_str[-i]
        subtrahend_number = '0'
        if i <= len(num2_str):
            subtrahend_number = num2_str[-i]

        if minuend_number == '1' and subtrahend_number == '0':
            if take_rank:
                difference[-i] = '0'
                take_rank = False
        elif minuend_number == '1' and subtrahend_number == '1':
            difference[-i] = '0'
        elif minuend_number == '0' and subtrahend_number == '0':
            pass
        elif minuend_number == '0' and subtrahend_number == '1':
            take_rank = True
            difference[-i] = '1'

    return int(''.join(difference))


def subtract_using_additional_code(minuend: List[str], subtrahend: List[str],
                                   bits=8) -> List[str]:
    """ Вычитание двочиных чисел c применением дополнительного кода.

    minuend: str уменьшаемое - двоичное число в виде списка из '0' и '1'
    subtrahend: str вычитаемое - двоичное число в виде списка из '0' и '1'
    """
    minuend = ''.join(minuend)
    subtrahend = ''.join(subtrahend)

    if len(minuend) < bits:
        minuend = ('0' * (bits - len(minuend))) + minuend
    if len(subtrahend) < bits:
        subtrahend = ('0' * (bits - len(subtrahend))) + subtrahend

    minuend_additional_code = list(minuend)
    subtrahend_additional_code = convert_to_additoinal_code(list(subtrahend),
                                                            False)

    difference = summa(minuend_additional_code, subtrahend_additional_code)

    if len(difference) > bits:
        return difference[1:]

    return difference


def muliply(multiplicanda: List[str],
            multiplier: List[str], bits=8) -> List[str]:
    """ Уножение целых двоичных чисел со знаком. Машинный метод. """
    multiplicanda = multiplicanda[:]
    multiplier = multiplier[:]

    assert (len(multiplicanda) <= bits and len(multiplier) <= bits,
            f'Длина числа не должна превышать {bits} разрядов')

    for i in multiplicanda:
        assert (i == '0' or i == '1', 'Числа должны состоять только из 0 и 1')
    for i in multiplier:
        assert (i == '0' or i == '1', 'Числа должны состоять только из 0 и 1')

    if len(multiplier) < bits:
        multiplier = (['0'] * (bits - len(multiplier))) + multiplier
    if len(multiplicanda) < bits:
        multiplicanda = (['0'] * (bits - len(multiplicanda))) + multiplicanda

    product_sign = str(int(multiplier[SIGN] != multiplicanda[SIGN]))
    partial_product = '0' * 2 * bits
    # множимое с выровненное со старшими разрядами частичного произведения
    aligned_multiplicanda = multiplicanda + (2*bits - len(multiplicanda)) * ['0']

    for i in range(1, bits + 1):
        if multiplier[-i] == '1':
            tmp = ''.join(summa(partial_product, aligned_multiplicanda, 2*bits))
            if len(tmp) < bits:
                tmp = ('0' * (bits - len(tmp))) + tmp

            # partial_product = tmp + partial_product[bits:]
            partial_product = tmp

        # сдвиг на разряд вправо
        partial_product = '0' + partial_product[:-1]

    if len(partial_product) < bits:
        partial_product = ('0' * (bits - len(partial_product))) + partial_product

    partial_product = list(partial_product)[bits:]
    partial_product[SIGN] = product_sign

    return list(partial_product)


def division(divident: List[str], divisor: List[str], bits=4) -> List[str]:
    """ Деление 8-разрядных двоичных неотрицательных чисел

    divident: делимое
    divisor: делитель
    quotient: частное
    """
    assert (len(divident) == len(divisor) == bits,
            "Возможна работа только с двоичными числами в форме записи со знаком")

    result_sign = '1' if divident[0] != divisor[0] else '0'

    assert (compare(divident, divisor) >= 1,
            "Делимое должно быть больше или равно чем делитель")

    divisor_additional_code = convert_to_additoinal_code(
        divisor, bits, force=True)

    assert len(divident) == len(divisor_additional_code)

    partial_remainder_sign = '0'
    partial_remainder = divident[:]

    double_bits = 2 * bits
    # добавление незначащих нулей для удвоения разрядов делимого
    partial_remainder = (double_bits - len(partial_remainder)) * ['0'] \
                        + partial_remainder

    # выравнивание делителя по делимому сдвигом влево
    divisor = divisor + (double_bits - len(divisor)) * ['0']

    divisor_additional_code = convert_to_additoinal_code(
        divisor, double_bits, force=True)

    quotient = []
    for i in range(bits):
        # сдвиг делимого влево на разряд
        partial_remainder = partial_remainder[1:] + ['0']

        # Если полученный остаток положительный, то после его сдвига на
        # один разряд влево к нему прибавляется делитель в ДК,
        # а если остаток отрицательный, то после сдвига влево к нему
        # прибавляется делитель в прямом коде
        if partial_remainder_sign == '1':
            partial_remainder = summa(partial_remainder[:],
                                      divisor[:], double_bits)
            if len(partial_remainder) > double_bits:
                partial_remainder = partial_remainder[1:]
        elif partial_remainder_sign == '0':
            partial_remainder = summa(partial_remainder[:],
                                      divisor_additional_code[:], double_bits)

        partial_remainder_sign = partial_remainder[SIGN]

        # Если полученный остаток положительный, то цифре частного
        # присваивается значение 1, а если остаток отрицательный,
        # то присваивается 0
        if partial_remainder_sign == '1':
            quotient.append('0')
        elif partial_remainder_sign == '0':
            quotient.append('1')

    if len(quotient) < (bits - 1):
        quotient = ['0'] * ((bits - 1) - len(quotient)) + quotient
        quotient.insert(0, result_sign)

    return quotient


def compare(num1: List[str], num2: List[str]) -> int:
    """ Сраннение двоичных чисел без знака.
    Возвращает 0 если числа равны.
    1 если первое число больше чем второе
    -1 если второе число больше чем первое
    """
    if len(num1) > len(num2) and num1[0] != '0' and num2[0] != '0':
        return 1
    elif len(num2) > len(num1) and num1[0] != '0' and num2[0] != '0':
        return -1

    for i in range(len(num1)):
        if num1[i] == '1' and num2[i] == '0':
            return 1
        elif num1[i] == '0' and num2[i] == '1':
            return -1

    return 0


def plus13(aa, bb):
    a = f'{aa:0>8b}'
    b = f'{bb:0>8b}'
    result = ['0'] * 8
    carry_bit = '0'
    for i in range(7, -1, -1):
        if a[i] == '1' and b[i] == '1':
            result[i] = carry_bit
            carry_bit = '1'
        elif (a[i] == '1' and b[i] == '0') or (a[i] == '0' and b[i] == '1'):
            if carry_bit == '0':
                result[i] = '1'
        else:
            if carry_bit == '1':
                result[i] = '1'
                carry_bit = '0'
    return int(''.join(result), 2)


def left_shift(number: List[str]) -> List[str]:
    """ Арифметический сдвиг влево

    Сдвиг, при котором уходящий бит исчезает, не влияя на оставшиеся биты,
    а на месте появившегося бита записывается бит 0.

    number - массив односимвольных строк из значений '0' и '1'
    """
    return number[1:] + ['0']
