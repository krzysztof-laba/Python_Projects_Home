class Animal():
    def __init__(self, name, age, hungry):
        print("Innit")
        self.name = name
        self.age = age
        self.is_hungry = hungry

    def get_mame(self):
        return self.name, self.age, self.is_hungry




zebra = Animal("Jeffrey", 26, True)
print(zebra, " To jest rezerwowana pamięć dla stworzonej instancji klasy.\n") # rezerwowana pamięć
print(zebra.get_mame())