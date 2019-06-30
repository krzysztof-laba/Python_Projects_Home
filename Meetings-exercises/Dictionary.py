student_name = {
                "Krzysztof": "name",
                "Monika": "ID",
                "Pawel":125,
                "Wladek":111,
                "Johan":"opoka"
                }

for i in student_name.items():
    print("Cale: ", i)
print("----------------------")
for i in student_name.keys():
    print("Pierwsze: ", i)
print("----------------------")
for (i) in student_name.values():
    print("Drugie:", i)
print("----------------------")

print(student_name["Monika"])
print(student_name["Wladek"])
print(student_name["Johan"])

del student_name["Monika"]
print("Deleted one key with value:")
print(student_name)