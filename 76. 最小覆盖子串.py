"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
"""

def minWindow(s, t):
    n = len(s)
    if len(t) > n: return ""
    if n == 1:
        if s == t:
            return s
        else:
            return ""
    p0, p1, res, ans = 0, 0, n, ""
    while p1 < n:
        p1 += 1
        content = s[p0:p1]
        cur_len = p1 - p0
        # print(cur_len, content,windowcheck(content, t))
        while windowcheck(content, t):
            if cur_len <= res:
                res, ans = cur_len, content
            p0 += 1
            content = s[p0:p1]
            cur_len = p1 - p0
    return ans

def windowcheck(content, t):
    for i in t:
        # print(content, t)
        if i not in content:
            return False
        if i in content:
            content = content.replace(i, "", 1)
    return True

print(minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(minWindow(s = "a", t = "a"))
print(minWindow(s = "a", t = "aa"))
print(minWindow(s = "a", t = "b"))
print(minWindow(s = "ab", t = "b"))
print(minWindow(s = "aa", t = "aa"))