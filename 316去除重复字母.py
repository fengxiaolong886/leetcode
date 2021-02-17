"""
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters 相同
"""

def removeDuplicateLetters(s):
    stack = []
    for idx, char in enumerate(s):
        if char in stack:
            continue
        while stack and char < stack[-1] and stack[-1] in s[idx:]:
            stack.pop()
        stack.append(char)
    return "".join(stack)
print(removeDuplicateLetters(s = "bcabc"))
print(removeDuplicateLetters(s = "cbacdcbc"))
print(removeDuplicateLetters(s = "bbcaac"))


