def move(x, direction="right", list_input=[]):
    if direction == "right":
        first = list_input[-x:]
        second = list_input[:-x]
        right_move = first + second
        print(right_move)
    elif direction == "left":
        first = list_input[:x]
        second = list_input[x:]
        left_move = second + first
        print(left_move)


move(3, "right", [1, 2, 3, 4])
