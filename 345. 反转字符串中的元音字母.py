"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
"""

def reverseVowels(s):
    query = "aeiouAEIOU"
    vow = []
    idx = []
    for i, j in enumerate(s):
        if j in query:
            vow.append(j)
            idx.append(i)
    vow = vow[::-1]
    s = list(s)
    for i, j in zip(idx, vow):
        s[i] = j
    return "".join(s)

print(reverseVowels("hello"))
print(reverseVowels("leetcode"))