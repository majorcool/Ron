def play_way():  # 选择游戏模式，simple是不删除棋子，difficult删除
    while True:
        Play_way = str(input("\033[1;31;40msimple is 1,difficult is 2:\033[0m"))
        if Play_way == "1" or Play_way == "2":
            return Play_way
        else:
            print("\033[1;31;40mXXXXXXOnly 1 and 2,simple is 1,simple is 2\033[0m")


def chess_board(chess_all_place_2):  # 棋子的总体位置
    print("Game---Tic-Tac-Toe---simple")  # 这是棋盘
    print("  %s |  %s  | %s " % (chess_all_place_2[0], chess_all_place_2[1], chess_all_place_2[2]))
    print("---- ----- ----")
    print("  %s |  %s  | %s " % (chess_all_place_2[3], chess_all_place_2[4], chess_all_place_2[5]))
    print("---- ----- ----")
    print("  %s |  %s  | %s " % (chess_all_place_2[6], chess_all_place_2[7], chess_all_place_2[8]))
    print("Please put the chess in the right place, from 1---9")
    return chess_all_place_2


