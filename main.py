from typing import List

from mathematic.arithmetic import summa
from mathematic.arithmetic import subtract_as_ints
from mathematic.arithmetic import muliply
from mathematic.arithmetic import division


if __name__ == '__main__':
    num1 = 100101
    num2 = 100100

    # print(f'{num1} + {num2} = {summa(list(str(num1)), list(str(num2)))}')

    # print(f'{num1} - {num2} = {subtract_as_ints(num1, num2)}')
    # print(f'{num1} * {num2} = {muliply(num1, num2)}')
    # print(f'{num1} / {num2} = {division(num1, num2)}')

    """
    Трудности:
    1. Вычитание нулей с использованием ДК
    2. Как определить переполнение?
    3. В каком формате реализовывать? Строки или инты
    4. 
    
    Алгоритм деления. YAzyki-i-sistema-programmirovaniya.pdf с. 62
    
    Альтернативный вариант - реализация алгоритмов на массиве char.
    В питоне это будет массив из 0 и 1.  
    """
