"""

给你一个字符串 s，由若干单词组成，单词之间用空格隔开。返回字符串中最后一个单词的长度。如果不存在最后一个单词，请返回 0 。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
"""

def lengthOfLastWord(s):
    s_ = s.strip().split(" ")
    if len(s_) > 0:
        return len(s_[-1])
    else:
        return 0

print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord(" "))