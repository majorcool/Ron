# 6.1.6 定义一个函数，参数为 1 个字符串，将 a-z, A-Z 改为 z-a, Z-A，返回新的字符串
# 例如，参数为 'abcABC'，返回 'zyxZYX'
def happy(n):
    n = n.swapcase()
    long = len(n) - 1
    abc = "abcdefghijklmnopqrstuvwxyz"
    ll = []
    for l in range(0, long):
        ll.append(n[l])
    for a in range(0, long):
        num = n[a]
        w = abc.find(num)
        w = abc[-w]
        ll[a] = w
    for lll in range(0, long):
        print(ll[lll], end="")


happy("abcABC")
# leeues
# 不明白