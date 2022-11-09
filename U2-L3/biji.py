class Fruit:
    def __init__(self):  # 内置方法
        self.name = 'good'  # 实例属性
        self._price = '100'
        self.__real_name = 'bad'  # 私有实例属性+实例属性
        self.__real_price = '1'

    def __del__(self):
        pass

    def __rot(self):  # 私有实例方法
        print('no')

    def rot(self):  # 实例方法
        print('yes')

    def _secret(self):
        print(self.__real_name)

    def __another_secret(self):
        print(self.__real_name)
# 实例属性4(包括私有属性)                       !!!
# 实例方法4(不包含内置方法)
# 私有实列属性2
# 私有实例方法2
