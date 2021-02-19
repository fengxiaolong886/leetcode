"""
给定两个数组，编写一个函数来计算它们的交集。
"""

def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    res = []
    p0, p1 = 0, 0
    while p0 < len(nums1) and p1 < len(nums2):
        if nums1[p0] == nums2[p1]:
            res.append(nums2[p1])
            p0 += 1
            p1 += 1
        elif nums1[p0] > nums2[p1]:
            p1 += 1
        elif nums1[p0] < nums2[p1]:
            p0 += 1
    return res

print(intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
print(intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
