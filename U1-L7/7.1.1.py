# 7.1.1  定义一个函数，参数为 2 个字符串 s1，s2，判断 s1 是否可以通过打乱顺序来得到 s2，如果可以返回 True，不可以返回 False
def same(s1, s2):
    for c in range(0, len(s1)):
        if s2.find(s1[c]) == -1:
            print("False")
            break
    else:
        print("True")



same("bvc", "cvn")
