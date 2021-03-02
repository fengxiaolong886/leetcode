"""
配对交换。编写程序，交换某个整数的奇数位和偶数位，尽量使用较少的指令（也就是说，位0与位1交换，位2与位3交换，以此类推）。

示例1:

 输入：num = 2（或者0b10）
 输出 1 (或者 0b01)
示例2:

 输入：num = 3
 输出：3
"""

def exchangeBits(num):
    num_bin = list(str(bin(num)))
    if len(bin(num))%2 != 0:
        num_bin.insert(2,"0")
    for i in range(2, len(num_bin), 2):
        num_bin[i], num_bin[i+1] = num_bin[i+1], num_bin[i]
    res = "".join(num_bin)
    res = int(res, 2)
    return res

print(exchangeBits(1))
print(exchangeBits(2))
print(exchangeBits(3))
print(exchangeBits(7))