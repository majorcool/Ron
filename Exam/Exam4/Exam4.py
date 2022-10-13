def move(x, direction="right", list_input=[]):
    long = len(list_input) - x - 1
    have = []
    if direction == "right":
        for run in range(0, long+1):
            have.append(list_input[run])
        for l in range(0, long+1):
            l -= 1
            del(list_input[l])

        for a in range(0, len(list_input)-1):
            have.append(list_input[a])

        print(have)


move(2, "right", [1, 2, 3, 4, 5])





