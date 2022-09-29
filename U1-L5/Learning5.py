name_zhangsan = "zhangsan"
name_lisi = "lisi"
name_wangwu = "wangwu"
name_list = ["zhangsan","lisi","wangwu"]
print(name_list)

#1取值和索引
print(name_list[0])
print(name_list[1])
print(name_list[2])
#知道数据内容确定位置
#传递数据不在列表中---报错
print(name_list.index("lisi"))
#2修改
name_list[1] = "里斯"
print(name_list)
#3增加
name_list.append("网站小儿")#末尾添加
print(name_list)
name_list.insert(1,"小妹妹")#索引添加
print(name_list)
cxk = ["sing","dance","rap","basketball","chicken"]
name_list.extend(cxk)
print(name_list)
#其他列表追加当前列表
#4删除
name_list.remove("wangwu")#选择删除
print(name_list)
name_list.pop()
print(name_list)#pop默认删除最后一个
name_list.pop(3)
print(name_list)#pop可以指定
#name_list.clear()#清空
#print(name_list)

del name_list[1]#del把变量从内存中删除
print(name_list)
#用del把变量删除之后无法使用该变量

yz = len(name_list)#统计有几个变量
print(yz)

AAAA = name_list.count("zhangsan")#出现几次
print(AAAA)

big = ["b","a","c"]
the = ["36666666","9","222"]
#升序排序
the.sort()
big.sort()
print(the)
print(big)
#降序排序
the.sort(reverse=True)
big.sort(reverse=True)
print(the)
print(big)
#逆序
the.reverse()
big.reverse()
print(the)
print(big)
