# 6.2.4 罗马数字转换
# 定义一个函数，参数为一个字符串表示的罗马数字，返回对应的整数（输入的罗马数字不超过 1000）
# 罗马数字包含以下 7 种字符:I，V，X，L，C，D和M

def number_change(num):
    a = {"M": "1000", "D": "500", "C": "100", "L": "50", "X": "10", "V": "5", "I": "1"}
    b = {"CM": "900", "CD": "400", "XC": "90", "XL": "40", "IX": "9", "IV": "4"}
    num_z = 0
    # 如果遍历a,b的key再判断而不是先判断变量
    for key_special in b:  # 先遍历特殊值
        if num.find(key_special) != -1:
            num_z += int(b[key_special])
            num = num.removeprefix(key_special)
    while len(num) > 0:
        for key_common in a:  # 再遍历普通数, 每一个只判断一次的问题
            if num.find(key_common) != -1:
                num_z += int(a[key_common])
                num = num.removeprefix(key_common)
    return num_z


while True:
    n = str(input("罗马"))
    print(number_change(n))

