# def key_key(login_info):
#     user_1 = input("用户名")
#     list_0 = [user_1, "123456mm", "321654nn"]
#     tuple_0 = ()
#     for key in login_info:
#         if login_info[key] == user_1:
#             print("用户名正确")
#             while True:
#                 password = str(input("新密码,字母和数字"))
#                 if password == "q":
#                     print("False")
#                     break
#                 elif len(password) <= 8:
#                     print("密码应该达到8或8位以上")
#                     continue
#                 elif password.isalpha():
#                     print("应该有数字")
#                     continue
#                 elif password.isdigit():
#                     print("应该有字母")
#                     continue
#                 elif len(password) >= 8 and password.isalnum() == True:
#                     print("密码格式符合要求")
#                 for key in login_info:
#                     b = login_info[key]
#                     if b == password:
#                         print("请设置未使用过的密码")
#                         break
#                     elif b != password:
#                         break
#                 if b == password:
#                     continue
#                 elif b != password and len(list_0) < 4:
#                     list_0.insert(1, password)
#                     tuple_0 = list_0[0:len(list_0):1]
#                     print("已重置密码")
#                     break
#                 elif b != password and len(list_0) >= 4:
#                     list_0 = list_0[0:3:1]
#                     list_0.append(1, password)
#                     tuple_0 = list_0[0:4:1]
#                     print("已重置密码")
#                     break
#             return tuple_0
#
#
# login_info = {"user_1": "kun"}
# print(key_key(login_info))


def key_key(login_info):
    while True:
        user_name = str(input("input your name:"))
        if user_name == "q":
            return False
        if user_name not in login_info.keys():
            print("user name does not exist!")
            continue
        else:
            break
    while True:
        password = str(input("input your password"))
        if password == "q":
            return False
        if len(password) < 8:
            print("password must >= 8")
            continue
        if not password.isalnum():
            print("only numbers and alphabet!")
        if password in login_info[user_name]:
            print("password used recently!")
        else:
            break
    if len(login_info[user_name]) == 3:
        login_info[user_name].pop
    login_info[user_name].insert(0, password)
    print('password reset!')
    back = (user_name, login_info[user_name][0])
    return back


print(key_key({"user1": ["kunkunkun3", "1123456789a", "4n4449494945de06"]}))
