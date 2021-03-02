"""
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

美式键盘 中：

第一行由字符 "qwertyuiop" 组成。
第二行由字符 "asdfghjkl" 组成。
第三行由字符 "zxcvbnm" 组成。
"""

def findWords(words):
    keybord = ["qwertyuiop" ,"asdfghjkl" ,"zxcvbnm"]
    res = []
    for i in words:
        c1, c2, c3 = 0, 0, 0
        s = i.lower()
        for j in s:
            if j in keybord[0]: c1 += 1
            if j in keybord[1]: c2 += 1
            if j in keybord[2]: c3 += 1
        n = len(i)
        if c1 == n or c2 == n or c3 == n:
            res.append(i)
    return res




print(findWords(["Hello","Alaska","Dad","Peace"]))
print(findWords(["omk"]))
print(findWords(["adsdf","sfd"]))