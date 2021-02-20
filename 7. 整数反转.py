"""
给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。

"""

def reverse(x):
    x = str(x)
    if x[0] == "-":
        x = -int(x[1:][::-1])
    else:
        x = int(x[::-1])
    if x < -2**31 or x > (2**31 -1):
        return 0
    else:
        return x

print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(0))