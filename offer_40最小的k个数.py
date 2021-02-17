"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

"""
def getLeastNumbers(arr, k):
    arr.sort()
    return arr[:k]

print(getLeastNumbers(arr = [3,2,1], k = 2))
print(getLeastNumbers(arr = [0,1,2,1], k = 1))