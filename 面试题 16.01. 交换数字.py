"""
编写一个函数，不用临时变量，直接交换numbers = [a, b]中a与b的值。
"""

def swapNumbers(numbers):
    numbers[0], numbers[1] = numbers[1], numbers[0]
    return numbers

print(swapNumbers( numbers = [1,2]))