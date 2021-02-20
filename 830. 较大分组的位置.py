"""
在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。

例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。

分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx" 分组用区间表示为 [3,6] 。

我们称所有包含大于或等于三个连续字符的分组为 较大分组 。

找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。
"""

def largeGroupPositions(s):
    p0, p1, res = 0, 0, []
    while p0 or p1 < len(s):
        if s[p0] == s[p1] and p1 < len(s)-1:
            p1 += 1
        elif s[p0] == s[p1] and p1 == len(s) -1:
            if p1 - p0 >= 2:
                res.append([p0, p1])
            return res
        elif s[p0] != s[p1]:
            if p1 - p0 >=3:
                res.append([p0, p1-1])
            p0 = p1
            p1 = p0
    return res

print(largeGroupPositions(s = "aaa"))
print(largeGroupPositions(s = "abbxxxxzzy"))
print(largeGroupPositions(s = "abc"))
print(largeGroupPositions(s = "abcdddeeeeaabbbcd"))
print(largeGroupPositions(s = "aba"))