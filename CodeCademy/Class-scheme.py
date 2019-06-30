class Osoba:

    def __init__(self, imie, imie2): # konstruktor
        """
        Konstruktor klasy
        """
        self.imie = imie
        self.imie2 = imie2

    def __del__(self): # destruktor
        print("{0} mówi: Słabo mi....".format(self.imie))

print(" ")
print("Klasa istnieje i zajmuje pamięć:")
print(Osoba)                      # Clasa istnieje i zajumje pamięć

print(" ")
print("Tworzymy instancję klasy czyli obiekt:")
x = Osoba("Franek", "Krzys")      # TWORZENIE OBIEKTU (tzw. instancja klasy) Z KLASY

print(" ")
print("Wywołujemy atrybuty klasy:")
print(x.imie, x.imie2)            # WYWOŁANIE ATRYBUTU KLASY
print(x.imie2)

del x       # wywołanie destruktora