your_age = int(input("他的年龄："))
if 1 > your_age >= 0:
    print("他是婴儿")
elif 2 >= your_age >= 1:
    print("他是幼儿")
elif 12 >= your_age >= 3:
    print("他是儿童")
elif 16 >= your_age >= 13:
    print("他正处于青春期")
elif 24 >= your_age >= 17:
    print("他是年轻人")
elif 64 >= your_age >= 18:
    print("他是成年人")
elif your_age >= 65:
    print("他是老人")
else:
    print("他不是人")