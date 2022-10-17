def reset_password(login_info):
    # 判断用户名是否在字典的键中
    while user_name := input('input user name: '):
        if user_name == 'q':
            return False
        if user_name not in login_info.keys():
            print('user does not exist!')
        else:
            break

    # 强迫用户输入符合要求的密码：8 位字母数字、不在历史列表中
    while password := input('input new password: '):
        if password == 'q':
            return False
        if len(password) <= 8:
            print('length must > 8!')
            continue
        if not password.isalnum():
            print('only alphabet & nums!')
            continue
        if password in login_info[user_name]:
            print('password used recently!')
        else:
            break

    # 密码符合要求的情况下，判断需不需要删除原来的列表元素
    if len(login_info[user_name]) == 3:
        login_info[user_name].pop()

    # 添加密码
    login_info[user_name].insert(0, password)
    print('password reset!')
    return user_name, password, login_info[user_name]


login_infos = {'user1': ['pw1'], 'user2': ['pw3_now', 'pw2', 'pw1']}
while True:
    print(reset_password(login_infos))