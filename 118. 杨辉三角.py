"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
"""

def generate(numRows):
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    dp = [[0] * i for i in range(1, numRows+1)]
    dp[0] = [1]
    dp[1] = [1, 1]
    for i in range(2, numRows):
        dp[i][0], dp[i][-1] = 1, 1
        for j in range(1, i):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    return dp

print(generate(1))
print(generate(2))
print(generate(5))