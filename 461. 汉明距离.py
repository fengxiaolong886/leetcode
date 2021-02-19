'''
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:
输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。
'''

def hammingDistance(x, y):
    x, y = str(bin(x))[2:], str(bin(y))[2:]
    num = max(len(x), len(y))
    res = 0
    if len(x)  > len(y):
        xbin = list(x)
        ybin = [0] * (num - len(y)) +list(y)
    elif len(x)  <= len(y):
        xbin = [0] * (num - len(x)) +list(x)
        ybin = list(y)
    for (i, j) in zip(xbin, ybin):
        if int(i) != int(j):
            res += 1
    return res

print(hammingDistance( x = 1, y = 4))
print(hammingDistance( x = 4, y = 1))