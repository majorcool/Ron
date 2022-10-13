def key_key(login_info):
    user_1 = input("用户名")
    for key in login_info:
        if key == user_1:
            print("用户名正确")
            while True:
                password = input("新密码")
                if len(password) < 8:
                    print("密码不少于八位")
                    continue
                elif password.isalnum() != True:
                    if password.isalpha() == True:
                        print("数字")
                    else:
                        print("字母,不能有特殊符号")
                if password >= 8 and password.isalnum() == True:
                    break

