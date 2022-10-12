place_1 = " "
place_2 = " "
place_3 = " "
place_4 = " "
place_5 = " "
place_6 = " "
place_7 = " "
place_8 = " "
place_9 = " "


def chess_frame():
    print("Game---Tic-Tac-Toe")
    print("  %s |  %s  | %s " % (place_1, place_2, place_3))
    print("---- ----- ----")
    print("  %s |  %s  | %s " % (place_4, place_5, place_6))
    print("---- ----- ----")
    print("  %s |  %s  | %s " % (place_7, place_8, place_9))
    print("Please put the chess in the right place, from 1---9")


def chess_play():
    player = 1
    chess_all_place = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if player % 2 == 1:
        place_chess = int(input("Please input the chess place1-9："))
        chess_all_place[place_chess-1] = "X"



chess_frame()
chess_play()