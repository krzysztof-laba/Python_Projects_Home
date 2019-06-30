"Liczby ciągu Fibonacciego"

def Wpisz_liczbe():
    n = input("Podaj liczbe do Fibonacci'ego: ")
    stringexample = "!@#$%^&*()_+.,<>/?';:[{]}\|}]" #znaki których nie ma przyjmować.
    if n.isalpha() or n in stringexample: #sprawdza czy podany znak jest liczbą i czy należy do grupy znaków niechcianych
        print("Podany znak '{0}' nie jest liczbą.".format(n))
        Wpisz_liczbe()
    elif int(n) < 0: #jeśli mniejsze od zera wywołaj funkcję "Wpisz liczbę" jeszcze raz.
        print ("Podaj liczbę dodatnią.")
        Wpisz_liczbe()
    else: #warunek dla wyliczenia ciągu Fibonacciego.
        w = int(n)

        liczby_ciagu_fibonaciego = [] #inicjalizajca pustej listy

        #Warunek liczb początkowy ciągu
        x0 = 0
        x1 = 1

        if w == 0:
            liczby_ciagu_fibonaciego.append(x0) #do listy dodaj x0
            print(liczby_ciagu_fibonaciego)
        elif w == 1:
            liczby_ciagu_fibonaciego = [0]
            liczby_ciagu_fibonaciego.append(x1)
            print(liczby_ciagu_fibonaciego)
        elif w == 2:
            liczby_ciagu_fibonaciego = [0]
            liczby_ciagu_fibonaciego.append(1)
            liczby_ciagu_fibonaciego.append(1)
            print(liczby_ciagu_fibonaciego)
        elif w > 2:
            liczby_ciagu_fibonaciego = [0]
            liczby_ciagu_fibonaciego.append(1)
            for i in range(w - 1):
                x2 = x0 + x1
                liczby_ciagu_fibonaciego.append(x2)
                print(liczby_ciagu_fibonaciego)
                x0 = x1
                x1 = x2


Wpisz_liczbe()
