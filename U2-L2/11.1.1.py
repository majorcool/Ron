class Student:
    def __init__(self, name=str(), id=str()):
        self.name = name
        self.id = id
        self.course = list()

    def __del__(self):
        print("already del {}, {}".format(self.name, self.id))

    def __str__(self):
        return "name: {}\nid: {}".format(self.name, self.id)

    def __len__(self):
        return len(self.course)

    def get_course(self):
        return self.course


student_1 = Student("zhang", "123456789")



