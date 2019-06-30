print('hello Krzysztof in my new world')
def wpisz_liczbe():
    n = input("Wpisz liczbe: ")
    return int(n)



def obliczenia(n):
    if 0 <= int(n) <= 1:
        print("Silnia liczby: {0}! = 1".format(int(n)))
    elif int(n) < 0:
        print("Silnia liczby ujemnej nie istnieje!")
        obliczenia(wpisz_liczbe())
    else:
        silnia = 2
        for i in range(int(n)):
            silnia = silnia * i
            print(silnia)
            return(i + 1)




obliczenia(wpisz_liczbe())