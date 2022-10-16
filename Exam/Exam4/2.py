def key_key(login_info):
    user_1 = input("用户名")
    list_0 = [user_1, "123456mm", "321654nn"]
    tuple_0 = ()
    for key in login_info:
        if login_info[key] == user_1:
            print("用户名正确")
            while True:
                password = str(input("新密码,字母和数字"))
                if password == "q":
                    print("False")
                    break
                elif len(password) <= 8:
                    print("密码应该达到8或8位以上")
                    continue
                elif password.isalpha():
                    print("应该有数字")
                    continue
                elif password.isdigit():
                    print("应该有字母")
                    continue
                elif len(password) >= 8 and password.isalnum() == True:
                    print("密码格式符合要求")
                for key in login_info:
                    b = login_info[key]
                    if b == password:
                        print("请设置未使用过的密码")
                        break
                    elif b != password:
                        break
                if b == password:
                    continue
                elif b != password and len(list_0) < 4:
                    list_0.insert(1, password)
                    tuple_0 = list_0[0:len(list_0):1]
                    print("已重置密码")
                    break
                elif b != password and len(list_0) >= 4:
                    list_0 = list_0[0:3:1]
                    list_0.append(1, password)
                    tuple_0 = list_0[0:4:1]
                    print("已重置密码")
                    break
            return tuple_0


login_info = {"user_1": "kun"}
print(key_key(login_info))






