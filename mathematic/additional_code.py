from typing import List

from mathematic.arithmetic import summa


def convert_to_additoinal_code(number: List[str], bits: int = 8) -> List[str]:
    additional_code = number[:]

    if additional_code[0] == '0':
        return additional_code

    if len(additional_code) > bits:
        raise ValueError("Разрядность числа превышает максимальное число бит")
    additional_code = align_bits(number)

    if additional_code[0] != '1':
        raise ValueError("Полученое число не в двоичной с.с.")

    for i in range(len(additional_code)):
        if additional_code[i] == '0':
            additional_code[i] = '1'
        elif additional_code[i] == '1':
            additional_code[i] = '0'
        else:
            raise ValueError("Число должно быть в двоичной системе счисления")

    additional_code = list(str(summa(additional_code, ['1'])))

    if len(additional_code) < bits:
        raise Exception("")

    return additional_code


def align_bits(number: List[str], bits=8):
    """ Дополнение незначащими нулями до необходимого количества разрядов"""
    return ['0'] * (bits - len(number)) + number
