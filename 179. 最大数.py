'''
给定一组非负整数 nums，重新排列它们每个数字的顺序（每个数字不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

'''

def largestNumber(nums):
    s = [(str(i)) for i in nums]
    s=sorted(s, key=newrule)
    res = "".join(s)
    if int(res) == 0:
        return "0"
    return res

class newrule(str):
    def __lt__(x, y):
        return x+y > y+x


print(largestNumber(nums = [10,2]))
print(largestNumber(nums = [3,30,34,5,9]))
print(largestNumber(nums = [1]))
print(largestNumber(nums = [10]))
print(largestNumber(nums = [0, 0]))