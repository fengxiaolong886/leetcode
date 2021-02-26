"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
"""
def getRow(rowIndex):
    numRows = rowIndex + 1
    if numRows == 1:
        return [1]
    if numRows == 2:
        return [1, 1]
    dp = [[0] * i for i in range(1, numRows+1)]
    dp[0] = [1]
    dp[1] = [1, 1]
    for i in range(2, numRows):
        dp[i][0], dp[i][-1] = 1, 1
        for j in range(1, i):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    return dp[-1]

print(getRow(0))
print(getRow(1))
print(getRow(2))
print(getRow(3))
