'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
'''


def isValid(s):
    querydict = {")":"(","}":"{","]":"["}
    res = []
    for i in s:
        if res and i in querydict and res[-1] == querydict[i]:
            res.pop()
        else:
            res.append(i)
    return not res

print(isValid(s = "()"))
print(isValid(s = "()[]{}"))
print(isValid(s = "(]"))
print(isValid(s = "([)]"))
print(isValid(s = "{[]}"))
