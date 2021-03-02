"""

给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。


"""

def findComplement(num):
    numbin = list(str(bin(num)))
    for i in range(2, len(numbin)):
        if numbin[i] == "0":
            numbin[i] = "1"
        else:
            numbin[i] = "0"
    return int("".join(numbin),2)

print(findComplement(5))
print(findComplement(1))