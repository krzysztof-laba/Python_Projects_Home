def czwarta(fun):
    def wewn(liczba):
        print("Jestem funkcją wewnętrzną.")
        wynik = fun(liczba)
        return wynik ** 2
    return wewn

@czwarta
def pierwsza(n):
    wynik_1 = n *2
    print("Pierwsza:", wynik_1)
    return wynik_1

"Bez dekoratora było by:"
#pierwsza = czwarta(pierwsza)

print(pierwsza(5))