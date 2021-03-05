"""
编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例 1:

输入: 6
输出: true
解释: 6 = 2 × 3
示例 2:

输入: 8
输出: true
解释: 8 = 2 × 2 × 2
示例 3:

输入: 14
输出: false
解释: 14 不是丑数，因为它包含了另外一个质因数 7。
"""

def isUgly(num):
    if num <= 0:
        return False
    while abs(num) > 1:
        if num % 2 ==0 or num % 3 == 0 or num % 5 == 0:
            if num % 2 ==0:
                num = num // 2
            elif num % 3 == 0:
                num = num // 3
            elif num % 5 == 0:
                num = num // 5
        else:
            return False
    return True

print(isUgly(6))
print(isUgly(8))
print(isUgly(14))
print(isUgly(-2147483648))
