"""
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

"""

def repeatedSubstringPattern(s):
    news = s+s
    news = news[1:-1]
    return s in news


print(repeatedSubstringPattern("abab"))
print(repeatedSubstringPattern("aba"))
print(repeatedSubstringPattern("abcabcabcabc"))