"""
给你一个偶数长度的字符串 s 。将其拆分成长度相同的两半，前一半为 a ，后一半为 b 。

两个字符串 相似 的前提是它们都含有相同数目的元音（'a'，'e'，'i'，'o'，'u'，'A'，'E'，'I'，'O'，'U'）。注意，s 可能同时含有大写和小写字母。

如果 a 和 b 相似，返回 true ；否则，返回 false 。


"""

def halvesAreAlike(s):
    s = s.lower()
    n = len(s)
    meta = ["a", "e", "i", "o", "u"]
    left , right = 0, 0
    for i in range(int(n/2)):
        if s[i] in meta:
            left += 1
    for i in range(int(n/2), n):
        if s[i] in meta:
            right += 1
    return  left == right

print(halvesAreAlike(s = "book"))
print(halvesAreAlike(s = "textbook"))
print(halvesAreAlike(s = "MerryChristmas"))
print(halvesAreAlike(s = "AbCdEfGh"))