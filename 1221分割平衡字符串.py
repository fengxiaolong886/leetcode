"""
在一个 平衡字符串 中，'L' 和 'R' 字符的数量是相同的。

给你一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

返回可以通过分割得到的平衡字符串的 最大数量

"""

def balancedStringSplit(s):
    count = 0
    res = 0
    for i in s:
        if i == "L": count += 1
        if i == "R": count -= 1
        if count == 0:
            res += 1
    return res

print(balancedStringSplit(s = "RLRRLLRLRL"))
print(balancedStringSplit(s = "RLLLLRRRLR"))
print(balancedStringSplit(s = "LLLLRRRR"))
print(balancedStringSplit(s = "RLRRRLLRLL"))