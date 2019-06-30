from tkinter import *
root = Tk()


root.geometry("700x700+1100+200")
root.title("Oddanie Wyprawkowego")

Tops = Frame(root, width=300, height=20, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

Tops = Frame(root, width=20, height=400, bg="red", relief=SUNKEN)
Tops.pack(side=LEFT)

Tops = Frame(root, width=20, height=400, bg="black", relief=SUNKEN)
Tops.pack(side=RIGHT)

Tops = Frame(root, width=300, height=20, bg="blue", relief=SUNKEN)
Tops.pack(side=BOTTOM)

button_1 = Button(text="S T A R T", height=1, width=10, fg="red", bg="light blue")
button_1.place(x=10, y=10)

button_2 = Button(text="S T O P", height=1, width=10)
button_2.place(x=10, y=50)



root.mainloop()