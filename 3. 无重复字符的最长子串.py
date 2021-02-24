"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
"""
def lengthOfLongestSubstring(s):
    n = len(s)
    if n < 2:
        return n
    lookup = set()
    max_len, cur_len, left = 0, 0, 0
    for i in range(n):
        cur_len += 1
        while s[i] in lookup:
            lookup.remove(s[left])
            left += 1
            cur_len -= 1
        max_len = max(max_len, cur_len)
        lookup.add(s[i])
    return max_len

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(""))