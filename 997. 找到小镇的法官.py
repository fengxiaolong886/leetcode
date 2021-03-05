"""
在一个小镇里，按从 1 到 N 标记了 N 个人。传言称，这些人中有一个是小镇上的秘密法官。

如果小镇的法官真的存在，那么：

小镇的法官不相信任何人。
每个人（除了小镇法官外）都信任小镇的法官。
只有一个人同时满足属性 1 和属性 2 。
给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示标记为 a 的人信任标记为 b 的人。

如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。
"""

def findJudge(N, trust):
    if not trust and N == 1:
        return 1
    if not trust and N > 1:
        return -1
    s, t = set(), set()
    for i, j in trust:
        s.add(i)
        t.add(j)
    can = list(t-s)
    if not can:
        return -1
    cnt = []
    for i in can:
        ok = True
        for x in range(1,N+1):
            # print("test", x, i, [x, i] in trust)
            if [x, i] not in trust and x != i:
                ok = False
        if ok:
            cnt.append(i)
    if cnt and len(cnt) == 1:
        return cnt[0]
    else:
        return -1


print(findJudge(N = 5, trust = []))
print(findJudge(N = 1, trust = []))
print(findJudge(N = 2, trust = [[1,2]]))
print(findJudge(N = 3, trust = [[1,3],[2,3]]))
print(findJudge(N = 3, trust = [[1,3],[2,3],[3,1]]))
print(findJudge(N = 3, trust = [[1,2],[2,3]]))
print(findJudge(N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]))