# 6.2.6 Excel 列名称
# 定义一个函数，参数为一个正整数 columnNumber ，返回它在 Excel 表中相对应的列名称
# 123456, A1:1*26^5,+.....+6*26^0, "^n"=len(num)-1, while len(num)>0
def name(columnNumber):
    num = 0
    alphabet = {"A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6", "G": "7", "H": "8", "I": "9", "J": "10", "K": "11", "L": "12", "M": "13", "N": "14", "O": "15", "P": "16", "Q": "17", "R": "18", "S": "19", "T": "20", "U": "21", "V": "22", "W": "23", "X": "24", "Y": "25", "Z": "26"}
    while len(columnNumber) > 0:
        num += columnNumber[0]

# 不会
