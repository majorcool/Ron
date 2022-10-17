# 5.3.5 编写一个函数 update_dict(dict_sample)，功能如下
# 用户输入一个 key-value（分 2 次输入），value 为数字类型，key 为 str 类型
# 如果原有的 dict_sample 中没有用户输入的 key，就添加这个 key-value
# 如果原有的 dict_sample 中存在用户输入的 key，保留较大的 value
# 将修
# 改后的字典作为返回值
def update_dict(dict_sample):
    dict_key = str(input("请输入key类型为字符串"))
    dict_value = int(input("请输入value类型为数字"))
    for key in dict_sample:
        if key != dict_key:
            break
        else:
            if dict_value >= dict_sample[key]:
                break
            if dict_value < dict_sample[key]:
                break
    if key != dict_key:
        dict_add = {dict_key: dict_value}
        dict_sample.update(dict_add)
    else:
        if dict_value >= dict_sample[key]:
            dict_sample[key] = dict_sample[key]
        if dict_value < dict_sample[key]:
            dict_sample[key] = dict_add[key]
    return dict_sample
