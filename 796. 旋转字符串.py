"""
给定两个字符串, A 和 B。

A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。
如果在若干次旋转操作之后，A 能变成B，那么返回True。
"""

def rotateString(A, B):
    if len(B) < len(A):
        return False
    new = A + A
    new = new[1:-1]
    if B in new:
        return True
    else:
        return False

print(rotateString(A = 'abcde', B = 'cdeab'))
print(rotateString(A = 'abcde', B = 'abced'))
print(rotateString(A = 'aa', B = 'a'))