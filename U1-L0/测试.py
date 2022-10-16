chess_all_place = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

line_1 = chess_all_place[0:3:1]
line_2 = chess_all_place[3:6:1]
line_3 = chess_all_place[6:9:1]
rowe_1 = chess_all_place[0:7:3]
rowe_2 = chess_all_place[1:8:3]
rowe_3 = chess_all_place[2:9:3]
diagonal_1 = chess_all_place[0:9:4]
diagonal_2 = chess_all_place[2:7:2]
win_X = ["X", "X", "X"]
win_O = ["O", "O", "O"]
if line_1 == win_O:
    print(4)
if line_2 == win_O:
    print(5)
if line_3 == win_O:
    print(6)
if rowe_1 == win_O:
    print("1")
if rowe_2 == win_O:
    print("2")
if rowe_1 == win_O:
    print("3")
if diagonal_1 == win_O:
    print(7)
if diagonal_2 == win_O:
    print(8)
print(line_1)
print(line_2)
print(line_3)
print(rowe_1)
print(rowe_2)
print(rowe_3)
print(diagonal_1)
print(diagonal_2)