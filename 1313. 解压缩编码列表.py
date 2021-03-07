"""
给你一个以行程长度编码压缩的整数列表 nums 。

考虑每对相邻的两个元素 [freq, val] = [nums[2*i], nums[2*i+1]] （其中 i >= 0 ），每一对都表示解压后子列表中有 freq 个值为 val 的元素，你需要从左到右连接所有子列表以生成解压后的列表。

请你返回解压后的列表。

"""

def decompressRLElist(nums):
    res = []
    n = len(nums)
    for i in range(0, n, 2):
        res.extend([nums[i+1]] * (nums[i]))
    return res

print(decompressRLElist(nums = [1,2,3,4]))
print(decompressRLElist(nums = [1,1,2,3]))