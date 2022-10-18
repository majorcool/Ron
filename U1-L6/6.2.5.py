# 6.2.5 验证回文串
# 定义一个函数，参数为一个字符串 s
# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样，则可以认为该短语是一个 回文串
# 如果它是回文串 ，返回 True ；否则，返回 False
def a(s):
    s_ = ""
    for char in s:
        if char.isalnum():
            s_ += char.lower()
    return s_ == s_[::-1]  # s_[::-1]倒序


print(a("acacs"))