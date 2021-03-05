"""
面试题 05.06. 整数转换
整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。
"""

def convertInteger(A, B):
    return bin((A ^ B) & 0xffffffff).count('1')

print(convertInteger(29, 15))
print(convertInteger(1, 2))
print(convertInteger(826966453, -729934991))  #14

