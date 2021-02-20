#!/usr/bin/env bash
"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
"""

def strStr(haystack, needle):
    m , n = len(haystack), len(needle)
    if haystack == needle: return 0
    for i in range(m):
        if needle == haystack[i:i+n]:
            return i
    return -1

print(strStr(haystack = "hello", needle = "ll"))
print(strStr(haystack = "aaaaa", needle = "bba"))
