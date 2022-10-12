# 6.1.1 设计用例，尝试常用（加粗）的字符串方法，打印对应的结果

# 1replace() 返回字符串，其中指定的值被替换为指定的值
a = "123"
a = a.replace("123", "321")
print(a)

# jion() 把可迭代对象的元素连接到字符串的末尾
a = "123"
a = "X".join(a)
print(a)

# 变量.strip() 返回字符串的剪裁版本。
a = "    123321    "
a = a.strip()
print(a)

# 变量.lstrip() 返回字符串的左修剪版本（遍历删除）
a = "   123   "
a = a.lstrip()
print(a)

# 变量.rstrip() 返回字符串的右边修剪版本（遍历删除）
a = "   123   "
a = a.rstrip()
print(a)

# str.removeprefix() 返回字符串的左修剪版本（整体删除）删一个
a = "1111122233311"
a = a.removeprefix("1")
print(a)

# str.removesuffix() 返回字符串的右边修剪版本（整体删除）
a = "1111122233311"
a = a.removesuffix("1")
print(a)

# partition() 返回元组，其中的字符串被分为三部分
a = "11233211"
a = a.partition("2")
print(a)

# rpartition() 返回元组，其中字符串分为三部分
a = "11233211"
a = a.rpartition("2")
print(a)

# split(s,max) 在指定的分隔符处拆分字符串，并返回列表
a = "11   2332145654111"
a = a.split("1", 1)
print(a)

# rsplit(s,max) 在指定的分隔符处拆分字符串，并返回列表
a = "11   2332145654111"
a = a.rsplit("1", 1)
print(a)

# splitlines() 在换行符处拆分字符串并返回列表
a = "12312312\n34564896532"
a = a.splitlines()
print(a)

# count() 返回指定值在字符串中出现的次数
a = "11562599"
a = a.count("5")
print(a)

# find() 在字符串中搜索指定的值并返回它被找到的位置
a = "1569854265"
a = a.find("5", 4, 8)
print(a)

# startswith() 如果以指定值开头的字符串，则返回 true
a = "186532486"
b = "91353"
a = a.startswith("1")
b = b.startswith("1")
print(a)
print(b)

# endswith() 如果字符串以指定值结尾，则返回 true
a = "186532486"
b = "91353"
a = a.endswith("6")
b = b.endswith("1")
print(a)
print(b)

# isspace() 如果字符串中的所有字符都是空白字符，则返回 True
a = "                                                                         "
a = a.isspace()
print(a)

# isalpha() 如果字符串中的所有字符都在字母表中，则返回 True
a = "dbhjabcab1ahjbchacbj"
a = a.isalpha()
print(a)

# isalnum() 如果字符串中的所有字符都是字母数字，则返回 True
a = "16134845138165684513184"
a = a.isalnum()
print(a)

# isupper() 如果字符串中的所有字符都是大写，则返回 True
a = "YUKGYKGYG"
a = a.isupper()
print(a)

# islower() 如果字符串中的所有字符都是小写，则返回 True
a = "86851616518418cdccdefgukyuffhhg"
a = a.islower()
print(a)

# upper() 把字符串转换为大写
a = "jlinuhhkbjnclsVHG"
a = a.upper()
print(a)

# lower() 把字符串转换为小写
a = "BUILhnhbbhhh"
a = a.lower()
print(a)