"TWORZENIE KLAS"
class Calculator():

    def __init__(self): # Funkcja init wykonuje się przy tworzeniu instancji klasy.
        print("Init !!")

    def __del__(self): # Usuwanie/zwalnianie pamieci po wykonaniu clasy.
        print("Del !!")

    def __str__(self): # Konwertowanie na string i zwracamy 'Hallo' (można zwracać też liczbę np 10, 5) ;)
        return "Hallo"

    def __len__(self):
        return 100

    def __bool__(self):
        return True

    def dodaj(self, a, b):
        wynik = a + b
        print(wynik, " Dodane")

    def odejmij(self, a, b):
        wynik = a - b
        print(wynik, " Odjęte")

calc = Calculator() # TU JUŻ JEST REZERWOWANA PAMIĘĆ - instancja klasy
# print(calc) # Wyświetlenie zarezerwowanej pamieci
calc.dodaj(2, 3) # Wywołanie dodawania
# calc.odejmij(3, 2)

# calc_2 = Calculator()
# calc_2.dodaj(10, 20)

print(len(calc))