"""
给定一个整数，将其转化为7进制，并以字符串形式输出。
"""


def convertToBase7(num):
    res = ""
    if num == 0:
        return "0"
    if num < 0:
        flag = True
    else:
        flag = False
    num = abs(num)
    while num >= 1:
        num , tail = divmod(num, 7)
        res = str(tail) + res
    if flag:
        res = "-" + res
    return res

print(convertToBase7(100))
print(convertToBase7(-7))