"""
给你一个整数数组 salary ，数组里每个数都是 唯一 的，其中 salary[i] 是第 i 个员工的工资。

请你返回去掉最低工资和最高工资以后，剩下员工工资的平均值。
"""
def average(salary):
    salary.sort()
    salary.pop()
    salary.pop(0)
    return sum(salary)/len(salary)

print(average(salary = [4000,3000,1000,2000]))
print(average(salary = [1000,2000,3000]))
print(average(salary = [6000,5000,4000,3000,2000,1000]))
print(average(salary = [8000,9000,2000,3000,6000,1000]))