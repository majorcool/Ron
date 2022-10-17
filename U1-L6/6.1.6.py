# 6.1.6 定义一个函数，参数为 1 个字符串，将 a-z, A-Z 改为 z-a, Z-A，返回新的字符串
# 例如，参数为 'abcABC'，返回 'zyxZYX'
# def happy(n):
#     n = n.swapcase()
#     long = len(n) - 1
#     abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     ll = []
#     for l in range(0, long+1):
#         ll.append(n[l])
#     for a in range(0, long+1):
#         num = n[a]
#         w = abc.find(num)
#         w = abc[-(w+1)]
#         ll[a] = w
#     for lll in range(0, long+1):
#         print(ll[lll], end="")
#
#
# happy("zZa")
def back(n):
    forward = "abcdefghijklmnopqrstuvwxyz"
    backward = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return n.translate(str.maketrans(forward, backward))


print(back("guty"))