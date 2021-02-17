'''
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。
'''
def backspaceCompare(S,T):
    resS, resT = [], []
    for i in S:
        if i == "#" and resS:
            resS.pop()
        elif i != "#":
            resS.append(i)
    for i in T:
        if i == "#" and resT:
            resT.pop()
        elif i != "#":
            resT.append(i)
    ansS = "".join(resS)
    ansT = "".join(resT)
    if ansS == ansT:
        return True
    else:
        return False

print(backspaceCompare(S = "ab#c", T = "ad#c"))
print(backspaceCompare(S = "ab##", T = "c#d#"))
print(backspaceCompare(S = "a##c", T = "#a#c"))
print(backspaceCompare(S = "a#c", T = "b"))
print(backspaceCompare(S = "y#fo##f", T = "y#f#o##f"))

