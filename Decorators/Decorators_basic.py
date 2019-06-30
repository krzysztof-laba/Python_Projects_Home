"""
def decorator(f):
    def wrap(a, b):             # robimy dokładnie to samo, definiujemy funkcję zwracająca zwykła wartość.
        print('we wrapperze')
        return f(a, b)
    return wrap                 # dekorator zwraca funkcję o tej samej sygnaturze jak tą, którą dekorujemy.

@decorator
def foo(a, b):
    return a + b


print(foo(1, 2))
"""


def utworz_dodawanie(x):
    print("1.")

    def dodaj(y):
        print("2.")
        return x + y
    return dodaj


dodaj5 = utworz_dodawanie(5)
print("0.", dodaj5)
print("Wynik =", dodaj5(10))
