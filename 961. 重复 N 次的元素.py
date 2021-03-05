"""
在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。

返回重复了 N 次的那个元素。
"""
from collections import Counter
def repeatedNTimes(A):
    query = Counter(A)
    n = int(len(A)/2)
    for i in query:
        if query[i] == n:
            return i

print(repeatedNTimes([1,2,3,3]))
print(repeatedNTimes([2,1,2,5,3,2]))
print(repeatedNTimes([5,1,5,2,5,3,5,4]))