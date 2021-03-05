"""
给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）

以这种方式修改数组后，返回数组可能的最大和。
"""

def largestSumAfterKNegations(A, K):
    for i in range(K):
        A.sort()
        A[0] = -A[0]
    return sum(A)


print(largestSumAfterKNegations(A = [4,2,3], K = 1))
print(largestSumAfterKNegations(A = [3,-1,0,2], K = 3))
print(largestSumAfterKNegations(A = [2,-3,-1,5,-4], K = 2))
print(largestSumAfterKNegations(A = [-2,9,9,8,4], K = 5)) # 32