"""
稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。

示例1:

 输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
 输出：-1
 说明: 不存在返回-1。
示例2:

 输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
 输出：4
提示:

words的长度在[1, 1000000]之间
"""

def findString(words, s):
    if s not in words:
        return -1
    else:
        return words.index(s)

print(findString(words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"))
print(findString(words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"))