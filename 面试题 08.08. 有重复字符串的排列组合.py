"""
有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。

示例1:

 输入：S = "qqe"
 输出：["eqq","qeq","qqe"]
示例2:

 输入：S = "ab"
 输出：["ab", "ba"]
"""

from itertools import permutations
def permutation(S):
    return list(set(["".join(i) for i in permutations(list(S), len(S))]))

print(permutation(S = "qqe"))
print(permutation(S = "ab"))
