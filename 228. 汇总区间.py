"""
给定一个无重复元素的有序整数数组 nums 。

返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：

"a->b" ，如果 a != b
"a" ，如果 a == b

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/summary-ranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

def summaryRanges(nums):
    if not nums:return []
    if len(nums) == 1: return [str(nums[0])]
    res = []
    s , e = nums[0], nums[0]
    for i in range(1, len(nums)):
        if nums[i] -nums[i-1] != 1:
            e = nums[i-1]
            res.append([s, e])
            s, e = nums[i], nums[i]
        if i == len(nums) -1:
            e = nums[i]
            res.append([s, e])
    ans = []
    for x, y in res:
        if x == y:
            ans.append(str(x))
        else:
            ans.append("{0}->{1}".format(x, y))
    return ans



print(summaryRanges(nums = [0,1,2,4,5,7]))
print(summaryRanges(nums = [0,2,3,4,6,8,9]))
print(summaryRanges(nums = []))
print(summaryRanges(nums = [10]))
print(summaryRanges(nums = [10, 11]))
print(summaryRanges(nums = [10, 12]))