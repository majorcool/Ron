# 6.2.6 Excel 列名称
# 定义一个函数，参数为一个正整数 columnNumber ，返回它在 Excel 表中相对应的列名称
# 123456, A1:1*26^5,+.....+6*26^0, "^n"=len(num)-1, while len(num)>0
def name(columnNumber):
    line = ""
    alphabet = {"0": "A", "1": "B", "2": "C", "3": "D", "4": "E", "5": "F", "6": "G", "7": "H", "8": "I", "9": "J", "10": "K", "11": "L", "12": "M", "13": "N", "14": "O", "15": "P", "16": "Q", "17": "R", "18": "S", "19": "T", "20": "U", "21": "V", "22": "W", "23": "X", "24": "Y", "25": "Z"}
    while columnNumber > 0:
        if columnNumber > 0:
            line += alphabet[str((columnNumber - 1) % 26)]
            columnNumber = (columnNumber - 1) % 26
        if columnNumber > 0:
            line += alphabet[str(columnNumber // 26)]
            columnNumber = columnNumber // 26
    line = line[::-1]
    return line


while True:
    n = int(input("数字:"))
    print(name(n))

