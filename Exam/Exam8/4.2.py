# 4.2  列表乘积
# 定义一个函数，参数为一个只含整数的列表，判断列表所有元素的乘积的正负性
# 如果乘积大于零，返回 1；等于零，返回 0；小于零，返回 -1
# tip：把所有元素的乘积计算出来并不是个好主意
def array_sign(nums: list[int]) -> int:
    minus = 0
    for a in nums:
        if str(a)[0] == "-":
            minus += 1
        elif a == 0:
            return 0
    if minus % 2 == 0:
        return 1
    elif minus % 2 == 1:
        return -1


nums = [-1,1,-1,1,-1]
print(array_sign(nums))




