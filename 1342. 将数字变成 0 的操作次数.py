'''
给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。
'''

def numberOfSteps(num):
    res = 0
    while num:
        if num % 2 == 0:
            num = num / 2
            res += 1
        else:
            num -= 1
            res += 1
    return res

print(numberOfSteps(14))
print(numberOfSteps(8))
print(numberOfSteps(123))
