"""
给你一个字符串 s，它由数字（'0' - '9'）和 '#' 组成。我们希望按下述规则将 s 映射为一些小写英文字符：

字符（'a' - 'i'）分别用（'1' - '9'）表示。
字符（'j' - 'z'）分别用（'10#' - '26#'）表示。 
返回映射之后形成的新字符串。

题目数据保证映射始终唯一。
"""
def freqAlphabets(s):
    query = {}
    for i in range(1, 27):
        query[i] = chr(i + 96)
    query[0] = 0
    i = 0
    res = []
    while i < len(s):
        if s[i] != "#":
            res.append(query[int(s[i])])
        if s[i] == "#":
            res.pop()
            res.pop()
            res.append(query[int(s[i-2:i])])
        i += 1
    return "".join(res)




print(freqAlphabets(s = "10#11#12"))
print(freqAlphabets(s = "1326#"))
print(freqAlphabets(s = "25#"))
print(freqAlphabets(s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))