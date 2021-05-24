from typing import List

# from mathematic.additional_code import convert_to_additoinal_code

SIGN = 0  # индекс знакового разряда


def invert_sign(number: List[str]):
    number = number[:]
    if number[0] == '0':
        number[0] = '1'

    return convert_to_additoinal_code(number)


def convert_to_additoinal_code(number: List[str], bits: int = 8) -> List[str]:
    ones_complement = number[:]
    # print("Число: ", number)

    if ones_complement[
        0] == '0':  # Дополнительный код положительного числа совпадает с прямым кодом.
        return ones_complement

    if len(ones_complement) > bits:
        raise ValueError("Разрядность числа превышает максимальное число бит")

    ones_complement = ['0'] * (len(ones_complement) - bits) + ones_complement

    # if additional_code[0] != '1':
    #     raise ValueError("Полученое число не в двоичной с.с.")

    # Для отрицательного числа все цифры числа заменяются на противоположные (1 на 0, 0 на 1),
    for i in range(len(ones_complement)):
        if ones_complement[i] == '0':
            ones_complement[i] = '1'
        elif ones_complement[i] == '1':
            ones_complement[i] = '0'
        else:
            raise ValueError("Число должно быть в двоичной системе счисления")
    # ones_complement[0] = '1'  # в знаковый разряд заносится единица.

    # print("Обратный код: ", ones_complement)

    additional_code = summa(ones_complement, ['1'])

    if len(additional_code) < bits:
        raise Exception("")
        minuend_additional_code = ('0' * (
                bits - len(ones_complement))) + ones_complement
    # print("Дополнительный код: ", additional_code)

    # https://neerc.ifmo.ru/wiki/index.php?title=%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F_%D0%B2%D1%8B%D1%87%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D1%8F_%D1%81%D1%83%D0%BC%D0%BC%D0%B0%D1%82%D0%BE%D1%80%D0%BE%D0%BC
    return additional_code


def summa(num1: List[str], num2: List[str], bits=8) -> List[str]:
    num1 = ''.join(num1)
    num2 = ''.join(num2)

    # уравнять числа по длине
    if len(num1) < bits:
        len_diff = bits - len(num1)
        num1 = '0' * len_diff + num1

    if len(num2) < bits:
        len_diff = bits - len(num2)
        num2 = '0' * len_diff + num2

    additional = False
    result = ''
    for i in range(1, len(num1) + 1):
        val1 = num1[-i]
        val2 = num2[-i]

        if val1 == '0' and val2 == '0':
            if additional:
                result = '1' + result
                additional = False
            elif not additional:
                result = '0' + result
        elif val1 == '0' and val2 == '1':
            if additional:
                result = '0' + result
                additional = True
            elif not additional:
                result = '1' + result
        elif val1 == '1' and val2 == '0':
            if additional:
                result = '0' + result
                additional = True
            elif not additional:
                result = '1' + result
        elif val1 == '1' and val2 == '1':
            if additional:
                result = '1' + result
                additional = True
            elif not additional:
                result = '0' + result
                additional = True

    if additional:
        result = '1' + result

    return list(result)


def subtract_as_ints(minuend: int, subtrahend: int) -> int:
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


def subtract_with_additional_code(minuend: List[str], subtrahend: List[str],
                                  bits=8) -> List[str]:
    """
    Вычитание двочиных чисел в дополнительном коде
    minuend: str уменьшаемое - двоичное число в виде строки
    subtrahend: str вычитаемое - двоичное число в виде строки
    """
    minuend = ''.join(minuend)
    subtrahend = ''.join(subtrahend)

    bits = 8
    if len(minuend) < bits:
        minuend = ('0' * (bits - len(minuend))) + minuend
    if len(subtrahend) < bits:
        subtrahend = ('0' * (bits - len(subtrahend))) + subtrahend

    minuend_additional_code = list(minuend)
    subtrahend_additional_code = list(subtrahend)
    subtrahend_additional_code = convert_to_additoinal_code(
        subtrahend_additional_code)

    difference = summa(minuend_additional_code, subtrahend_additional_code)
    if len(difference) > 8:
        return difference[1:]

    return difference


def muliply(multiplicanda, multiplier) -> int:
    if isinstance(multiplicanda, list):
        num1_str = ''.join(multiplicanda)
        num2_str = ''.join(multiplier)

    # TODO: Работа с массивом строк длины 1
    elif isinstance(multiplicanda, int):
        num1_str = str(multiplicanda)
        num2_str = str(multiplier)
    else:
        raise ValueError()

    assert (len(num1_str) <= 8 and len(num2_str) <= 8,
            'Длина числа не должна превышать 8 разрядов')
    for i in num1_str:
        assert (i == '0' or i == '1', 'Числа должны состоять только из 0 и 1')
    for i in num2_str:
        assert (i == '0' or i == '1', 'Числа должны состоять только из 0 и 1')

    if len(num2_str) < 8:
        num2_str = ('0' * (8 - len(num2_str))) + num2_str

    multiplicanda = list(str(multiplicanda))
    product = '0' * 16
    for i in range(1, len(num2_str) + 1):
        if num2_str[-i] == '1':
            tmp = str(summa(product[:8], multiplicanda))
            if len(tmp) < 8:
                tmp = ('0' * (8 - len(tmp))) + tmp
            product = tmp + product[8:]
            product = '0' + product[:-1]
        elif num2_str[-i] == '0':
            product = '0' + product[:-1]

    return int(product)


def division(divident: List[str], divisor: List[str], bits=8) -> List[str]:
    """ Деление 8-разрядных двоичных неотрицательных чисел

    divident: делимое
    divisor: делитель
    quotient: частное
    """
    assert (len(divident) == len(divisor) == bits,
            "Возможна работа только с двоичными числами в форме записи со знаком")

    result_sign = '1' if divident[0] != divisor[0] else '0'
    quotient = []
    # quotient = [result_sign]

    divisor_additional_code = convert_to_additoinal_code(divisor, bits)

    assert len(divident) == len(divisor_additional_code)

    divisor_max_bit = 7  # количество значащих битов
    for i in divisor[1:]:
        if i == '0':
            divisor_max_bit -= 1
            continue
        break

    divident_bits = 2*bits
    divident = divident[1:] + ['0']  # сдвиг делителя влево на разряд
    partial_remainder = summa(divident, divisor_additional_code, bits)
    for i in range(bits - divisor_max_bit):
        partial_remainder_sign = partial_remainder[SIGN]
        if partial_remainder[SIGN] == '1':
            quotient.append('0')
        else:
            quotient.append('1')

        partial_remainder = partial_remainder[1:] + ['0']
        quotient.insert(0, partial_remainder_sign)

        if partial_remainder_sign == '1':
            partial_remainder = summa(
                partial_remainder, divisor, len(partial_remainder))
        else:
            partial_remainder = subtract_with_additional_code(
                partial_remainder, divisor, len(partial_remainder))

        if compare(partial_remainder, divisor) == -1:
            break


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