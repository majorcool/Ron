def biggest(num_list):
    what_big = []
    for a in range(0,len(num_list)):
        for b in range(a+1, len(num_list)):
            for c in range(b+1, len(num_list)):
                abc = num_list[a] * num_list[b] * num_list[c]
                what_big.append(abc)
    return max(what_big)
n = [1,2,-3,-3,0]
print(biggest(n))