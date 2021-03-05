"""
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

注意：本题相对原题稍作改动
"""


def massage(nums):
    if not nums:
        return 0
    n = len(nums)
    if n < 3:
        return max(nums)
    dp = [0 for _ in range(n+1)]
    dp[1] = nums[0]
    ans = 0
    for i in range(2, n+1):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        ans = max(ans, dp[i])
    return ans

print(massage([1,2,3,1]))
print(massage([2,7,9,3,1]))
print(massage([2,1,4,5,3,1,1,3]))