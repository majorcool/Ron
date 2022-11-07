# 3. 排列
# 定义一个函数 perms(l)，参数为长度为 5 且只包含不重复元素的列表，返回所有的排列
# 思考：如果长度不固定，应该怎么做？
# tip：善用搜索 —— 开发者的基本能力之一
import itertools


def perms(l: list) -> list:
    return list(itertools.permutations(l, len(l)))


print(perms([1, 2, 3, 4, 5]))
