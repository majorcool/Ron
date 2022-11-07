# 11.3.6  定义 Student 类和 Course 类
# Student 类
# 3 个属性 id，name，courses
#   courses 是一个列表，保存着若干课程的 id
# 2 个实例方法 add_course()，del_course()
#   add_course() 可以添加 1 个课程；del_course() 可以删除 1 个课程
# 定义构造函数（constructor）和析构函数（destructor）
# Course 类
# 3 个属性 id，name，students
#   students 是一个列表，保存着若干学生的 id
# 2 个实例方法 add_student()，del_student()
#   add_student() 可以添加 1 个学生；del_course() 可以删除 1 个学生
# 定义构造函数（constructor）和析构函数（destructor）
class Student:
    def __init__(self, id, name, courses):
        self.id = id
        self.name = name
        self.course = courses

    def add_course(self, a):
        self.course.append(a)

    def del_course(self, d):
        self.course.remove(d)

    def __del__(self):
        print("已删除{}".format(self.d))


class Course:
    def __init__(self, id, name, students):
        self.id = id
        self.name = name
        self.students = students

    def add_students(self, a):
        self.students.append(a)

    def del_students(self, d):
        self.students.remove(d)

    def __del__(self):
        print("已删除{}".format(self.d))