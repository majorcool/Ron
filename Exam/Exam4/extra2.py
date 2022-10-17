def long_word(s):
    a = s.partition(" ")
    b = a[len(a)-1]
    print(b)


long_word("happy have")