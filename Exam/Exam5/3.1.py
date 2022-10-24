def password(user_info):
    a = 0
    b = 0
    c = 0
    while True:
        password_0 = str(input("请输入旧密码:"))
        password_1 = str(input("请输入新密码:"))
        password_2 = str(input("请输入新密码:"))
        for old in user_info:
            older = user_info[old]
            if older != password_0:
                print("原密码不正确!")
                break
            elif older == password_0:
                name = old
        if older != password_0:
            continue
        if password_1 != password_2:
            print("新密码不一致!")
            continue
        if len(password_1) < 8:
            print("新密码不少于8位")
            continue
        for d in range(0, len(password_1)):
            only = str(password_1[d])
            if only.isalnum():
                a = 1
            if only.islower():
                b = 1
            if only.isupper():
                c = 1
        if a + b + c >= 2:
            user_info[name] = password_1
            print("修改成功!")
            return True
        if a + b + c < 2:
            print("只能使用数字，小写字母和大写字母，且至少包含其中两种!")


user_info = {"xk": "12345678n"}
print(password(user_info))