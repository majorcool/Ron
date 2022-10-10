# 5.3.3 下方是一个字典，按要求完成操作
# ① 字典的长度是多少
# ② 请修改 'java' 这个 key 对应的 value 值为 98
# ③ 删除 c 这个 key
# ④ 增加一个 key-value 对，key 值为 php, value 是 90
# ⑤ 获取所有的 key 值，存储在列表里
# ⑥ 获取所有的 value 值，存储在列表里
# ⑦ 判断 javascript 是否在字典中
# ⑧ 获得字典里所有 value 的和
# ⑨ 获取字典里最大的 value
# ⑩ 获取字典里最小的 value
# ⑪ 字典 dic1 = {'php': 97}，将 dic1 的数据更新到 dic 中
dic = {
    'python': 95,
    'java': 99,
    'c': 100
}
print(len(dic))

dic["java"] = 98
print(dic)

dic.pop("c")
print(dic)

dic["php"] = 90
print(dic)

list_0 = []
for key in dic:
    list_0.append(key)
print(list_0)

list_1 = []
for value in dic:
    list_1.append(dic[key])
print(list_1)

print("javascript" in dic)

num = 0
for value in dic:
    num += dic[key]
print(num)

list_2 = []
for value in dic:
    list_2.append(dic[key])
max_num = max(list_2)
print(max_num)

list_3 = []
for value in dic:
    list_3.append(dic[key])
min_num = min(list_2)
print(min_num)

dic1 = {"php": 97}
dic.update(dic1)
print(dic)