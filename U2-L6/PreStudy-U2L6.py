# 1. 什么是多继承？
# 子类可以拥有多个父类，并且具有所有父类的属性和方法

# 2. 如果子类继承自多个父类，且父类中具有相同名称的方法，子类会选择哪个父类的方法执行？
# __mro__ 可以查看方法 索顺序，从左到右
# 继承的顺序class C(A, D, B):顺序ADB
