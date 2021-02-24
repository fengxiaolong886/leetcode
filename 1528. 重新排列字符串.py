"""
给你一个字符串 s 和一个 长度相同 的整数数组 indices 。

请你重新排列字符串 s ，其中第 i 个字符需要移动到 indices[i] 指示的位置。

返回重新排列后的字符串。
"""

def restoreString(s, indices):
    res = []
    for (i, j ) in zip(indices, list(s)):
        res.append((i, j))
    res.sort()
    ans = []
    for (i, j) in res:
        ans.append(j)
    return "".join(ans)

print(restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
print(restoreString(s = "abc", indices = [0,1,2]))
print(restoreString(s = "aiohn", indices = [3,1,4,2,0]))
print(restoreString(s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]))
print(restoreString(s = "art", indices = [1,0,2]))