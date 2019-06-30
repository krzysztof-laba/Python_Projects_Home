students = []

class Student:
    def add_student(self, name = "Krzysztof", student_id = 333): #funkcja użyta z dodawania do listy. Krzysztof i 333 to defaultowe ustawienie.
        student = {"name": name, "student_id": student_id}
        students.append(student)
    def napis(self, zdanie):
        print(zdanie)

# student = Student()
# print(student)
#
# new_student = Student()
# print(new_student)


student = Student()
student.add_student("Ja", 5)
print(students)

Student().napis("Moja pierwsza próba ciekawe czy jak dodam więcej to też wyjdzie")