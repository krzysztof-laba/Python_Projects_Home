"TWORZENIE ZMIENNYCH W KLASACH"
class Calculator():

    def __init__(self): # Funkcja init wykonuje się przy tworzeniu instancji klasy.
        self.ostatni_wynik = 0 # Tworzymy tutaj np zmienne.

    def dodaj(self, a, b):
        wynik = a + b
        self.ostatni_wynik = wynik
        print(wynik, " Dodane")

    def odejmij(self, a, b):
        wynik = a - b
        self.ostatni_wynik = wynik
        print(wynik, " Odjęte")

calc = Calculator()
calc.dodaj(5, 2)    # Instancja klasy
calc.dodaj(100, 50)
calc.odejmij(100, 50)
print("Ostatni wynik to: {}.".format(calc.ostatni_wynik))