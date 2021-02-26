"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

 

示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
示例 2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
示例 3：

输入：digits = [0]
输出：[1]
"""

def plusOne(digits):
    digits = [str(i) for i in digits]
    digits = list(str(int("".join(digits))+1))
    digits = [int(i) for i in digits]
    return digits


print(plusOne(digits = [1,2,3]))
print(plusOne(digits = [4,3,2,1]))
print(plusOne(digits = [0]))
print(plusOne(digits = [9]))
print(plusOne(digits = [9, 9]))
print(plusOne(digits = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]))
print(plusOne(digits = [1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]))
