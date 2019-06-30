students = []

class Student:

    school_name = "L0 1"

    def __init__(self, name = "Krzysztof", id = 333):
        self.name = name
        self.id = id
        students.append(self)

    def __str__(self):
        return "Student " + self.name + " " + str(self.id)

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


marzena = Student("marzena", 3)

print(marzena.get_name_capitalize())
print(Student.school_name)


student = Student()
student.get_name_capitalize()
