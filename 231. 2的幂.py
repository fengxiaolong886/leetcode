"""
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

"""

def isPowerOfTwo(n):
    if n == 1:
        return True
    if n < 1:
        return False
    while n >1:
        check = n % 2
        if check != 0:
            return False
        n = n // 2
    return True


print(isPowerOfTwo(0))
print(isPowerOfTwo(1))
print(isPowerOfTwo(16))
print(isPowerOfTwo(218))