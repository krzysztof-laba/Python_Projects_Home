lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30]
lista.append(50)
print("Append:", lista)
lista.insert(1, 100)
print("Insert:", lista)
print("Value from list under index 1 =", lista[1])

print("\nIterate through the 'lista':")
for i in lista:
    print("Value:", i, "index:", lista.index(i))
    if i == 10:
        print("Continue")
        continue
    elif i == 20:
        print("Break and no value after 20.")
        break

print("\nRange from value = 5.")
value = 5
x = range(value)
print(x)
for i in range(value):
    print(i)

print("Check if value is in 'lista'.")
value = 10
print(value in lista)
