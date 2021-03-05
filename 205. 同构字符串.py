"""
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

"""
from collections import defaultdict
def isIsomorphic(s, t):
    query1 = defaultdict(set)
    query2 = defaultdict(set)
    for i, j in zip(s, t):
        query1[i].add(j)
        query2[j].add(i)
    for i in query1:
        if len(query1[i]) > 1:
            return False
    for i in query2:
        if len(query2[i]) > 1:
            return False
    return True


print(isIsomorphic(s = "egg", t = "add"))
print(isIsomorphic(s = "foo", t = "bar"))
print(isIsomorphic(s = "paper", t = "title"))
print(isIsomorphic(s = "badc", t = "baba"))
print(isIsomorphic(s = "paper", t = "title"))  #true