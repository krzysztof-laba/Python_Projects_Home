student_name = ["Krzysztof", "Monika", "Pawel", "Wladek", "Johan"]
for i in student_name:
    if i == "Pawel":
        print("Found", i)
        break #przerywa iterację pętli
    print("Still searching")

print("----------------------")

for i in student_name:
    if i == "Monika":
        continue #kontynuuje następną iterację pętli
        print("Found", i)
    print("Still searching", i)