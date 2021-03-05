"""
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。

顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。

如果你能给每位顾客正确找零，返回 true ，否则返回 false 。
"""

def lemonadeChange(bills):
    pocket = [0, 0, 0]
    for i in bills:
        if i == 5: pocket[0] += 1
        if i == 10: pocket[1] += 1
        if i == 20: pocket[2] += 1
        back = i -5
        if back == 5:
            pocket[0] -= 1
            if pocket[0] < 0:
                return False
        if back == 15:
            if pocket[1] > 0 and pocket[0] > 0:
                pocket[0] -= 1
                pocket[1] -= 1
            elif pocket[0] >= 3:
                pocket[0] -= 3
            else:
                return False
    return True


print(lemonadeChange([5,5,5,10,20]))
print(lemonadeChange([5,5,10]))
print(lemonadeChange([10,10]))
print(lemonadeChange([5,5,10,10,20]))
print(lemonadeChange([5,5,5,10,5,5,10,20,20,20]))  #false
