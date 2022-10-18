# 6.2.1 计算最后一个单词的长度
# 定义一个函数，参数是一个字符串 s，由若干单词组成，单词前后用一些空格隔开
# 返回字符串中最后一个单词的长度
# s 仅有英文字母和空格 ' ' 组成；s 中至少存在一个单词
def long_word(s):
    a = s.partition(" ")
    b = a[len(a)-1]
    print(b)


long_word("happy have")