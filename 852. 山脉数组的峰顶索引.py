"""
符合下列属性的数组 arr 称为 山脉数组 ：
arr.length >= 3
存在 i（0 < i < arr.length - 1）使得：
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
给你由整数组成的山脉数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i 。
"""

def peakIndexInMountainArray(arr):
    res = []
    for i in range(1, len(arr)-1):
        if arr[i-1] < arr[i]  and arr[i] > arr[i+1]:
            res.append(i)
    return res[0]

print(peakIndexInMountainArray([0,1,0]))
print(peakIndexInMountainArray([0,2,1,0]))
print(peakIndexInMountainArray([0,10,5,2]))
print(peakIndexInMountainArray([3,4,5,1]))