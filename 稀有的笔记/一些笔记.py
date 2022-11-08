"""
def a(x,y):
def a(x,y=XXX):
可变def a(x, * y):元组(把x参数后面的全变成y的元组)
关键字def a(x, ** y):字典
必选，可选，可变，关键字
def 顺序(a,b=1,*c,**d)
"""


def maybe(a, * b):
    print(b)


maybe(1, [2, 3], 1)


def must(c, ** d):
    print(d)


must(1, a={1, 2}, b=(1,3), f={1:([3,5],2)})


def add(x: int, y: int) -> int:  # 标注x,y,返回值的类型，这只是一个注释，结果不同没有任何影响
    return x + y

# f(n) = 2f(n-1)+1


"""
递归：只需要公式如f(n)=f(n-1)+f(n-1)+1(汉诺塔游戏)，不需要编写具体的做法(f()的具体公式)
"""

"""
析构函数：删除类中的对象是执行的方法
class C
删除class中c1 = C()
当没有对象映射到那个内存时才会调用析构方法
"""