"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

 

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
"""

def longestCommonPrefix(strs):
    ans = ""
    for i in zip(*strs):
        if len(set(i)) == 1:
            ans += i[0]
        else:
            break
    return ans


print(longestCommonPrefix(strs = ["flower","flow","flight"]))
print(longestCommonPrefix(strs = ["dog","racecar","car"]))
print(longestCommonPrefix(strs = ["ab", "a"]))
print(longestCommonPrefix(strs = []))
print(longestCommonPrefix(strs = [""]))