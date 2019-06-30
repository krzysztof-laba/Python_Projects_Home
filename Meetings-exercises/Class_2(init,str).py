students = []

class Student:
    def __init__(self, name = "Krzysztof", student_id = 333): #name i id to ustawienia defaultowe
        student = {"name": name, "student_id": student_id}
        students.append(student)
    def __str__(self):                      #Overwrite method in object. Nadpisz metodę w obiekcie.
        return "Student"


marzena = Student("wacek", 1)

print(students)
print(marzena)