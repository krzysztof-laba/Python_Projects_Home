from tkinter import *
# okno = Tk()
# etykieta = Label(okno, text="Hej!", font=("Arial",24,"italic"),foreground="yellow", background="blue")
# etykieta.pack()
# okno.mainloop()


lista = [(1, 5, "kajfd", 25, (200, 400)),
         (1, 3, "three"),
         (2, 6),
         (2, 5, "pozycja", [22, 33, "4444"]),
         (2, 4),
         (2, 3)]

print(lista[3])
print(lista[3][3][2])
print(lista[0][4][1])



strings = "Ala ma kota | Kot ma Ale | 5 | 0 | DISABLED"


# Name, Position, Label, Init value, Values
list_parameters = [("Checkbox 1", 1, "Time sleep before expeditions (min.):", 0, ["Set 24", "Set 25", "Set 26", "Set 37"]),
                   ("Checkbox 2", 2, "Dress up the expedition's equipment.", 1, ["Set 1", "Set 2", "Set 3", "Set 4"]),
                   ("Checkbox 3", 3, "Give back the expedition's equipment.", 1, ["Set 3", "Set 3", "Set 3", "Set 3"]),
                   ("Checkbox 4", 4, "Log off the browser.", 0, ["Set 300", "Set 400", "Set 500", "Set 600"])]

for i in list_parameters:
    print("*******")
    print(i)
    print(i[0])
    # print(i[1])
    # print(i[2])
    # print(i[3])
    # print(i[4])
    print(i[4][0])
    # print(i[4][1])
    # print(i[4][2])
    # print(i[4][3])
