student = {
    "name":"Mark",
    "student_id": 15164
}
student["last_name"] = "Kowalski"
try:
    last_name = student["last_name"]
    number_last_name = 3 + last_name
except KeyError:
    print("Error finding :)")
except TypeError:
    print("Nie mozna dodac 3 do stringa")
except Exception:
    print ("nieznany blad")

print("Code execuded!!!!!")