def Yes_or_No(): # Zapytanie czy chcemy dodać kolejną osobę.
    print("Dodać kolejną osobę? Wybierz 'Y' lub 'N' ")
    i = input()
    if i.lower() == "y":
        dodawanie_do_listy()
    else:
        print("Koniec")


def dodawanie_do_listy():
    plik = open("Moja lista.txt", "r")
    print("Lista studentów odczytana z pliku 'Moja lista'") # Wyświetlane po linice "plik" bo try/except sprawdza wew. aż dojdzie do warunku występowania pliku

    # Wygodniejsze wczytywanie z istniejącego pliku"
    for line in plik:
        print(line, end='')
    plik.close()

    # Dopisanie listy studentów: imię, nazwisko, grupa
    name = input("\nPodaj imię: ")  # '\n' dodaje/naciska ENTER. By wszystko w jednej linie nie było.
    surname = input("Podaj nazwisko: ")
    id = input("Podaj grupę: ")
    plik = open("Moja lista.txt", "a")  # 'a' - dodaje do listy kolejne dane nie nadpisując a dopisując na końcu.
    plik.write("\n" + name + ", " + surname + ", " + id)
    plik.close()
    print("Podaną osobę dopisano do 'Moja lista'")

    Yes_or_No() # wywołanie funcku Yes_or_No


def tworzenie_listy():
    headline = "Imie, Nazwisko, Grupa"
    plik = open("Moja lista.txt", "a") # 'a' - dodaje do listy kolejne dane nie nadpisując a dopisując na końcu.
    print("Plik 'Moja lista' nie istnieje. Dodaj osobę (imię, nazwisko, grupę) by stworzyć plik.") # Wyświetlane po linice "plik" bo try/except sprawdza wew. aż dojdzie do warunku występowania pliku
    name = input("\nPodaj imię: ")  # '\n' dodaje/naciska ENTER. By wszystko w jednej linie nie było.
    surname = input("Podaj nazwisko: ")
    id = input("Podaj grupę: ")
    # plik = open("Moja lista.txt", "a")  # 'a' - dodaje do listy kolejne dane nie nadpisując a dopisując na końcu.
    plik.write(headline + "\n" + name + ", " + surname + ", " + id)
    plik.close()

    Yes_or_No() # wywołanie funcji Yes_or_No

if __name__ == '__main__':
    try:
        dodawanie_do_listy()
    except:
        tworzenie_listy()