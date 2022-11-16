# 16.1.3  矩阵对角线之和
# 定义一个函数，参数为一个矩阵（二维列表）matrix，返回对角线所有元素的和
# 如果出现重复的中心元素，只计算一次
#  定义一个函数，参数为一个矩阵（二维列表）matrix，返回对角线所有元素的和
#  如果出现重复的中心元素，只计算一次
def matrix_diagonal_sum(matrix: list[list[int]]) -> int:
    # sum = 0
    # if len(matrix) % 2 == 0:
    #     for i in range(0, len(matrix)):
    #         sum = sum + matrix[i][i] + matrix[i][len(matrix) - i - 1]
    #     return sum
    # else:
    #     for i in range(0, len(matrix)):
    #         sum = sum + matrix[i][i] + matrix[i][len(matrix) - i - 1]
    #     sum = sum - matrix[int(((len(matrix)) + 1)/2 - 1)][int(((len(matrix)) + 1)/2 - 1)]
    #     return sum
    sum = 0
    for i in range(len(matrix)):
        if 2 * i + 1 != len(matrix):  # 若是奇数宫格在第三行地三列时2*2+1 == 5
            sum += matrix[i][i] + matrix[i][-(i+1)]
        else:
            sum += matrix[i][i]
    return sum


print(matrix_diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

