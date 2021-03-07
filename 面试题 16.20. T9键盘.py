"""
在老式手机上，用户通过数字键盘输入，手机将提供与这些数字相匹配的单词列表。每个数字映射到0至4个字母。给定一个数字序列，实现一个算法来返回匹配单词的列表。你会得到一张含有有效单词的列表。映射如下图所示：



示例 1:

输入: num = "8733", words = ["tree", "used"]
输出: ["tree", "used"]
示例 2:

输入: num = "2", words = ["a", "b", "c", "d"]
输出: ["a", "b", "c"]
"""
def getValidT9Words(num, words):
    query = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    pool = []
    for i in num:
        pool.append(query[int(i)-2])
    res = []
    for x in words:
        flag = True
        for i, j in zip(x,pool):
            if i not in j:
                flag = False
        if flag:
            res.append(x)
    return res

print(getValidT9Words(num = "8733", words = ["tree", "used"]))
print(getValidT9Words(num = "2", words = ["a", "b", "c", "d"]))


