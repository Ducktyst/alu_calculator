
def division(divident: List[str], divisor: List[str], bits=8) -> List[str]:
    """ Деление 8-разрядных двоичных неотрицательных чисел

    divident: делимое
    divisor: делитель
    quotient: частное
    """
    assert len(divident) == len(divisor) == bits

    result_sign = '1' if divident[0] != divisor[0] else '0'
    quotient = [result_sign]

    divisor_additional_code = convert_to_additoinal_code(divisor, bits)

    highest_value_bit = ...
    divisor_offsets_count = len(divident) - len(divisor)
    # divisor.extend(['0'] * divisor_offsets_count)

    assert len(divident) == len(divisor_additional_code)

    divident = divident[1:] + ['0'] # сдвиг влево на разряд

    partial_remainder = summa(divident, divisor_additional_code, bits)
    for i in range(divisor_offsets_count):
        partial_remainder_sign = partial_remainder[0]
        if partial_remainder_sign == '1':
            quotient.append('0')
        else:
            quotient.append('1')

        partial_remainder = partial_remainder[1:] + ['0']
        partial_remainder.insert(0, partial_remainder_sign)

        if partial_remainder_sign == '1':
            partial_remainder = summa(partial_remainder, divisor,
                                      len(partial_remainder))
        else:
            partial_remainder = subtract_with_additional_code(partial_remainder,
                                                              divisor, len(
                    partial_remainder))

        if compare(partial_remainder, divisor) == -1:
            break

    if len(quotient) < bits:
        quotient = ['0'] * (bits - len(quotient)) + quotient

    return quotient