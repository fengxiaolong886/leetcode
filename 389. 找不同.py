"""
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。
"""

def findTheDifference(s, t):
    s = "".join(sorted(list(s)))
    t = "".join(sorted(list(t)))
    for i in range(len(s)):
        if s[i] != t[i]:
            return t[i]
    return t[-1]




print(findTheDifference(s = "abcd", t = "abcde"))
print(findTheDifference(s = "", t = "y"))
print(findTheDifference(s = "a", t = "aa"))
print(findTheDifference(s = "ae", t = "aea"))