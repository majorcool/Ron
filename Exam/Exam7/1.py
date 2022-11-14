# 4.1  最大公约数 Pro Max
# 定义一个函数，参数为 n 个整数（1 <= n），返回这 n 个整数的最大公约数
# 还记得辗转相除法吗？虽然不记得了，但还是要往下看 :)
# 求 n 个数的最大公约数，只需要使用辗转相除法的拓展：
# 1. 将 n 个整数 d1 ... dn 从大到小排序
# 2. 如果 d1 能被 d2 整除，则令 d1 = d2，否则令 d1 = d1 - d2
# 3. 重复步骤 2，直至列表遍历完毕
# 4. 重复步骤 1 ~ 3，直至列表中所有数字都相等，此时这个数字即为这 n 个数的最大公约数
# 采用 2 种方法实现，第 1 种：递归，第 2 种：非递归
def greatest_common_divisor(n):
    while n[0] != n[len(n)-1]:
        n.sort(reverse=True)
        for num in range(0, len(n)-1):
            if n[num] % n[num+1] == 0:
                n[num] = n[num+1]
            else:
                n[num] = n[num] - n[num+1]
    return n[0]


a = [999, 1999, 2999, 3999, 4999]
print(greatest_common_divisor(a))


def greatest_common_divisor_2(b):
    b.sort(reverse=True)
    if b[0] == b[len(b)-1]:
        return b[0]
    for num in range(0, len(b)):
        if b[num] % b[num + 1] == 0:
            b[num] = b[num + 1]
            return greatest_common_divisor_2(b)
        else:
            b[num] = b[num] - b[num + 1]
            return greatest_common_divisor_2(b)


b = [1, 2, 3, 4, 5]
print(greatest_common_divisor_2(b))