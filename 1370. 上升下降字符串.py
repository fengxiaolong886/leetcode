'''
给你一个字符串 s ，请你根据下面的算法重新构造字符串：

1 从 s 中选出 最小 的字符，将它 接在 结果字符串的后面。
2 从 s 剩余字符中选出 最小 的字符，且该字符比上一个添加的字符大，将它 接在 结果字符串后面。
3 重复步骤 2 ，直到你没法从 s 中选择字符。
4从 s 中选出 最大 的字符，将它 接在 结果字符串的后面。
5从 s 剩余字符中选出 最大 的字符，且该字符比上一个添加的字符小，将它 接在 结果字符串后面。
6重复步骤 5 ，直到你没法从 s 中选择字符。
7 重复步骤 1 到 6 ，直到 s 中所有字符都已经被选过。
在任何一步中，如果最小或者最大字符不止一个 ，你可以选择其中任意一个，并将其添加到结果字符串。

请你返回将 s 中字符重新排序后的 结果字符串

'''

from collections import Counter
def sortString(s):
    res = []
    counts = Counter(s)
    totalch = list(set(s))
    flag = True
    while flag:
        totalch.sort()
        for i in totalch:
            if counts[i] > 0:
                res.append(i)
                counts[i] -= 1

        totalch.sort(reverse=True)
        for i in totalch:
            if counts[i] > 0:
                res.append(i)
                counts[i] -= 1
        flagcheck = 0
        for i in totalch:
            flagcheck += counts[i]
        if flagcheck == 0:
            flag = False
            return "".join(res)




print(sortString("aaaabbbbcccc"))
print(sortString("rat"))
print(sortString("leetcode"))
print(sortString("ggggggg"))
print(sortString("spo"))