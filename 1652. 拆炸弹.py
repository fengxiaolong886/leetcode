"""
你有一个炸弹需要拆除，时间紧迫！你的情报员会给你一个长度为 n 的 循环 数组 code 以及一个密钥 k 。

为了获得正确的密码，你需要替换掉每一个数字。所有数字会 同时 被替换。

如果 k > 0 ，将第 i 个数字用 接下来 k 个数字之和替换。
如果 k < 0 ，将第 i 个数字用 之前 k 个数字之和替换。
如果 k == 0 ，将第 i 个数字用 0 替换。
由于 code 是循环的， code[n-1] 下一个元素是 code[0] ，且 code[0] 前一个元素是 code[n-1] 。

给你 循环 数组 code 和整数密钥 k ，请你返回解密后的结果来拆除炸弹！
"""

def decrypt(code, k):
    n = len(code)
    res = []
    if k > 0:
        for i in range(n):
            res.append(sum([code[(j+i+1)%n] for j in range(k)]))
    if k == 0:
        res = [0 for i in range(n)]
    if k < 0:
        for i in range(n):
            res.append(sum([code[i-j-1] for j in range(-k)]))
    return res

print(decrypt(code = [5,7,1,4], k = 3))
print(decrypt(code = [1,2,3,4], k = 0))
print(decrypt(code = [2,4,9,3], k = -2))