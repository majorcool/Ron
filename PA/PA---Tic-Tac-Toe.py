# 有一个莫名其妙的问题……
import os
print("Please change 'Edit Run/Debug configurations' setting to PA---Tic-Tac-Toe")
chess_all_place = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # 棋子的总体位置
cut_num = []  # 记录并删除第七颗棋子的时机，位置
step = 1  # 判断玩家奇数为P1偶数为P2
while True:
    if len(cut_num) == 6:
        cut_near = int(cut_num[0]) + 1
        print("\033[1;31;40mXXXXXXafter next step, %d place's chess will be cut\033[0m" % cut_near)
    if len(cut_num) == 7:
        cut_near = int(cut_num[0]) + 2
        print("\033[1;31;40mXXXXXXafter next step, %d place's chess will be cut\033[0m" % cut_near)
    if len(cut_num) > 6:
        cut = int(cut_num[0])
        chess_all_place[cut] = " "
        del cut_num[0]
    if step % 2 == 1:
        print("Game---Tic-Tac-Toe")  # 这是棋盘
        print("  %s |  %s  | %s " % (chess_all_place[0], chess_all_place[1], chess_all_place[2]))
        print("---- ----- ----")
        print("  %s |  %s  | %s " % (chess_all_place[3], chess_all_place[4], chess_all_place[5]))
        print("---- ----- ----")
        print("  %s |  %s  | %s " % (chess_all_place[6], chess_all_place[7], chess_all_place[8]))
        print("Please put the chess in the right place, from 1---9")
        chess_place = str(input("Player1,X:"))
        if chess_place.isdigit() == False or len(chess_place) != 1 or chess_place == "0":  # 禁止用户乱输入字母和超长数字，和0为第九位的bug
            os.system("cls")  # clear
            print("\033[1;31;40mXXXXXXYou can only chess1-9\033[0m")
            continue
        chess_place = int(chess_place)
        if chess_all_place[chess_place - 1] == "X" or chess_all_place[chess_place - 1] == "O":
            os.system("cls")  # clear
            print("\033[1;31;40mXXXXXXChess's places can't be same\033[0m")
            continue
        chess_all_place[chess_place - 1] = "X"
        cut_num.append(chess_place - 1)
        step += 1
        os.system("cls")  # clear
    elif step % 2 == 0:
        print("Game---Tic-Tac-Toe")  # 这是棋盘
        print("  %s |  %s  | %s " % (chess_all_place[0], chess_all_place[1], chess_all_place[2]))
        print("---- ----- ----")
        print("  %s |  %s  | %s " % (chess_all_place[3], chess_all_place[4], chess_all_place[5]))
        print("---- ----- ----")
        print("  %s |  %s  | %s " % (chess_all_place[6], chess_all_place[7], chess_all_place[8]))
        print("Please put the chess in the right place, from 1---9")
        chess_place = str(input("Player2,O:"))
        if chess_place.isdigit() == False or len(chess_place) != 1:
            os.system("cls")  # clear
            print("\033[1;31;40mXXXXXXYou can only chess1-9\033[0m")
            continue
        chess_place = int(chess_place)
        if chess_all_place[chess_place - 1] == "X" or chess_all_place[chess_place - 1] == "O":
            os.system("cls")  # clear
            print("\033[1;31;40mXXXXXXChess's places can't be same\033[0m")
            continue
        chess_all_place[chess_place - 1] = "O"
        cut_num.append(chess_place - 1)
        step += 1
        os.system("cls")  # clear
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
    if line_1 == win_X or line_2 == win_X or line_3 == win_X or rowe_1 == win_X or rowe_2 == win_X or rowe_3 == win_X or diagonal_1 == win_X or diagonal_2 == win_X:
        print("XXXXXXPlayer1 win!!!")
        print("Game---Tic-Tac-Toe")
        print("  %s |  %s  | %s " % (chess_all_place[0], chess_all_place[1], chess_all_place[2]))
        print("---- ----- ----")
        print("  %s |  %s  | %s " % (chess_all_place[3], chess_all_place[4], chess_all_place[5]))
        print("---- ----- ----")
        print("  %s |  %s  | %s " % (chess_all_place[6], chess_all_place[7], chess_all_place[8]))
        break
    if line_1 == win_O or line_2 == win_O or line_3 == win_O or rowe_1 == win_O or rowe_2 == win_O or rowe_3 == win_O or diagonal_1 == win_O or diagonal_2 == win_O:
        print("XXXXXXPlayer2 win!!!")
        print("Game---Tic-Tac-Toe")
        print("  %s |  %s  | %s " % (chess_all_place[0], chess_all_place[1], chess_all_place[2]))
        print("---- ----- ----")
        print("  %s |  %s  | %s " % (chess_all_place[3], chess_all_place[4], chess_all_place[5]))
        print("---- ----- ----")
        print("  %s |  %s  | %s " % (chess_all_place[6], chess_all_place[7], chess_all_place[8]))
        break
