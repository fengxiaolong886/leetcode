"""
给你一个数组 items ，其中 items[i] = [typei, colori, namei] ，描述第 i 件物品的类型、颜色以及名称。

另给你一条由两个字符串 ruleKey 和 ruleValue 表示的检索规则。

如果第 i 件物品能满足下述条件之一，则认为该物品与给定的检索规则 匹配 ：

ruleKey == "type" 且 ruleValue == typei 。
ruleKey == "color" 且 ruleValue == colori 。
ruleKey == "name" 且 ruleValue == namei 。
统计并返回 匹配检索规则的物品数量 。

 

示例 1：

输入：items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
输出：1
解释：只有一件物品匹配检索规则，这件物品是 ["computer","silver","lenovo"] 。
示例 2：

输入：items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
输出：2
解释：只有两件物品匹配检索规则，这两件物品分别是 ["phone","blue","pixel"] 和 ["phone","gold","iphone"] 。注意，["computer","silver","phone"] 未匹配检索规则。
"""

def countMatches(items, ruleKey, ruleValue):
    res = 0
    condition = ["type", "color", "name"]
    if ruleKey == condition[0]:
        for i in items:
            if i[0] == ruleValue:
                res += 1
    if ruleKey == condition[1]:
        for i in items:
            if i[1] == ruleValue:
                res += 1
    if ruleKey == condition[2]:
        for i in items:
            if i[2] == ruleValue:
                res += 1
    return res

print(countMatches(items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],
                   ruleKey = "color",
                   ruleValue = "silver"))
print(countMatches(items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],
                   ruleKey = "type",
                   ruleValue = "phone"))
