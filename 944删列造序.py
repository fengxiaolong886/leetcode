"""
给你由 n 个小写字母字符串组成的数组 strs，其中每个字符串长度相等。

这些字符串可以每个一行，排成一个网格。例如，strs = ["abc", "bce", "cae"] 可以排列为：

abc
bce
cae
你需要找出并删除 不是按字典序升序排列的 列。在上面的例子（下标从 0 开始）中，列 0（'a', 'b', 'c'）和列 2（'c', 'e', 'e'）都是按升序排列的，而列 1（'b', 'c', 'a'）不是，所以要删除列 1 。

返回你需要删除的列数。
"""
from collections import defaultdict
def minDeletionSize(strs):
    res = defaultdict(list)
    ans = 0
    for i in strs:
        for idx, ch in enumerate(i):
            res[idx].append(ch)
    for i in res:
        test = "".join(res[i])
        if test != "".join(sorted(test)):
            ans += 1
    return ans



print(minDeletionSize(strs = ["cba","daf","ghi"]))
print(minDeletionSize(strs = ["a","b"]))
print(minDeletionSize(strs = ["zyx","wvu","tsr"]))