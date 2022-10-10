
def three(num_list):
    result = []
    for num_1 in range(0, len(num_list)-2):
        for num_2 in range(num_1+1, len(num_list)-1):
            for num_3 in range(num_2+1, len(num_list)):
                x = num_list[num_1]
                y = num_list[num_2]
                z = num_list[num_3]
                if x + y + z == 0:
                    result.append(tuple(sorted((x, y, z))))
                    list(set(result))
    return result


#2664946444
n = [-1, 0, 1, 2, -1, -4]
# print(three(n))
# import os
# os.system('clear')
