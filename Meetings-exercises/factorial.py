"Silnia zrobiona na while"
n = input("Wpisz liczbe: ")
int(n)

i = 1
silnia = 1
while i <= int(n):
    print(i)
    silnia = silnia * i
    i = i + 1

print("Silnia liczby", n, "to: ", silnia)