"""
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。

注意:

num 的长度小于 10002 且 ≥ k。
num 不会包含任何前导零。
"""


def removeKdigits(num, k):
    if len(num) <= k:
        return "0"
    stack = []
    remain = len(num) - k
    for i in num:
        while stack and k > 0 and i < stack[-1]:
            stack.pop()
            k -= 1
        stack.append(i)
    return "".join(stack[:remain]).lstrip("0") or "0"

print(removeKdigits(num="1234567890", k=9))
print(removeKdigits(num="112", k=1))
print(removeKdigits(num="10", k=1))
print(removeKdigits(num="425", k=1))
print(removeKdigits(num = "1432219", k = 3))
print(removeKdigits(num = "10200", k = 1))
print(removeKdigits(num = "10", k = 2))