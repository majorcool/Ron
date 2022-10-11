your_age = int(input("他的年龄："))
if 1 > your_age >= 0:
    print("他是婴儿")
elif 3 > your_age >= 1:
    print("他是幼儿")
elif 13 > your_age >= 3:
    print("他是儿童")
elif 17 > your_age >= 13:
    print("他正处于青春期")
if 24 >= your_age >= 17:
    print("他是年轻人")
if 65 > your_age >= 18:
    print("他是成年人")
elif your_age >= 65:
    print("他是老人")
else:
    print("他不是人")