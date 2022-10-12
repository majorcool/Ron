print("Game---Tic-Tac-Toe")
while True:
    step = 0
    player = 1
    chess_1 = " "
    chess_2 = " "
    chess_3 = " "
    chess_4 = " "
    chess_5 = " "
    chess_6 = " "
    chess_7 = " "
    chess_8 = " "
    chess_9 = " "
    print(" %s  " % chess_1, end="|")
    print("  %s  " % chess_2, end="|")
    print("  %s  " % chess_3)
    print("---- ----- ----")
    print(" %s  " % chess_4, end="|")
    print("  %s  " % chess_5, end="|")
    print("  %s  " % chess_6)
    print("---- ----- ----")
    print(" %s  " % chess_7, end="|")
    print("  %s  " % chess_8, end="|")
    print("  %s  " % chess_9)
    chess_all = [1,2,3,4,5,6,7,8,9]
    while step < 9:

        if player % 2 == 1 and step < 9:
            chess_place = int(input("请输入您的棋子的位置1-9，当前游玩者player1："))
            if chess_all[chess_place-1] == 0:
                print("请不要输入重复位置")
                continue
            if chess_place == 1:
                chess_1 = "X"
                player += 1
                del chess_all[0]
                chess_all.insert(0,0)
            elif chess_place == 2:
                chess_2 = "X"
                player += 1
                del chess_all[1]
                chess_all.insert(1, 0)
            elif chess_place == 3:
                chess_3 = "X"
                player += 1
                del chess_all[2]
                chess_all.insert(2, 0)
            elif chess_place == 4:
                chess_4 = "X"
                player += 1
                del chess_all[3]
                chess_all.insert(3, 0)
            elif chess_place == 5:
                chess_5 = "X"
                player += 1
                del chess_all[4]
                chess_all.insert(4, 0)
            elif chess_place == 6:
                chess_6 = "X"
                player += 1
                del chess_all[5]
                chess_all.insert(5, 0)
            elif chess_place == 7:
                chess_7 = "X"
                player += 1
                del chess_all[6]
                chess_all.insert(6, 0)
            elif chess_place == 8:
                chess_8 = "X"
                player += 1
                del chess_all[7]
                chess_all.insert(7, 0)
            elif chess_place == 9:
                chess_9 = "X"
                player += 1
                del chess_all[8]
                chess_all.insert(8, 0)
            else:
                print("请重新输入")
                continue
            step += 1
            print(" %s  " % chess_1, end="|")
            print("  %s  " % chess_2, end="|")
            print("  %s  " % chess_3)
            print("---- ----- ----")
            print(" %s  " % chess_4, end="|")
            print("  %s  " % chess_5, end="|")
            print("  %s  " % chess_6)
            print("---- ----- ----")
            print(" %s  " % chess_7, end="|")
            print("  %s  " % chess_8, end="|")
            print("  %s  " % chess_9)
            line_1 = chess_1 + chess_2 + chess_3
            line_2 = chess_4 + chess_5 + chess_6
            line_3 = chess_7 + chess_8 + chess_9
            list_1 = chess_1 + chess_4 + chess_7
            list_2 = chess_4 + chess_5 + chess_6
            list_3 = chess_7 + chess_8 + chess_9
            incline_1 = chess_1 + chess_5 + chess_9
            incline_2 = chess_3 + chess_5 + chess_7
            if line_1 == "XXX" or line_2 == "XXX" or line_3 == "XXX" or list_1 == "XXX" or list_2 == "XXX" or list_3 == "XXX" or incline_1 == "XXX" or incline_2 == "XXX":
                print("Player1 win")
                break
        if player % 2 == 0 and step < 9:
            chess_place = int(input("请输入您的棋子的位置1-9，当前游玩者player2："))
            if chess_all[chess_place-1] == 0:
                print("请不要输入重复位置")
                continue
            if chess_place == 1:
                chess_1 = "O"
                player += 1
                del chess_all[0]
                chess_all.insert(0, 0)
            elif chess_place == 2:
                chess_2 = "O"
                player += 1
                del chess_all[1]
                chess_all.insert(1, 0)
            elif chess_place == 3:
                chess_3 = "O"
                player += 1
                del chess_all[2]
                chess_all.insert(2, 0)
            elif chess_place == 4:
                chess_4 = "O"
                player += 1
                del chess_all[3]
                chess_all.insert(3, 0)
            elif chess_place == 5:
                chess_5 = "O"
                player += 1
                del chess_all[4]
                chess_all.insert(4, 0)
            elif chess_place == 6:
                chess_6 = "O"
                player += 1
                del chess_all[5]
                chess_all.insert(5, 0)
            elif chess_place == 7:
                chess_7 = "O"
                player += 1
                del chess_all[6]
                chess_all.insert(6, 0)
            elif chess_place == 8:
                chess_8 = "O"
                player += 1
                del chess_all[7]
                chess_all.insert(7, 0)
            elif chess_place == 9:
                chess_9 = "O"
                player += 1
                del chess_all[8]
                chess_all.insert(8, 0)
            else:
                print("请重新输入")
                continue
            step += 1
            print(" %s  " % chess_1, end="|")
            print("  %s  " % chess_2, end="|")
            print("  %s  " % chess_3)
            print("---- ----- ----")
            print(" %s  " % chess_4, end="|")
            print("  %s  " % chess_5, end="|")
            print("  %s  " % chess_6)
            print("---- ----- ----")
            print(" %s  " % chess_7, end="|")
            print("  %s  " % chess_8, end="|")
            print("  %s  " % chess_9)
            line_1 = chess_1 + chess_2 + chess_3
            line_2 = chess_4 + chess_5 + chess_6
            line_3 = chess_7 + chess_8 + chess_9
            list_1 = chess_1 + chess_4 + chess_7
            list_2 = chess_4 + chess_5 + chess_6
            list_3 = chess_7 + chess_8 + chess_9
            incline_1 = chess_1 + chess_5 + chess_9
            incline_2 = chess_3 + chess_5 + chess_7
            if line_1 == "OOO" or line_2 == "OOO" or line_3 == "OOO" or list_1 == "OOO" or list_2 == "OOO" or list_3 == "OOO" or incline_1 == "OOO" or incline_2 == "OOO":
                print("Player2 win")
                break


