el_list = [1, 2, 3, 4, 5, 6, 11]

print("\n*** I ***")
a, b, *c = el_list
print("b =", b)
print("c =", c)

print("\n*** II ***")
el_list_2 = [(1, 2), ("Ala", "Kot")]
for first, second in el_list_2:
    print(first, "->", second)

print("\n*** III ***")
# Iteration through the two lists:
names = ["Ala", "Ola", "Tomek", "Bartek"]
animals = ["kot", "pies", "chomik"]
for name, animal in zip(names, animals):
    print("Name:", name, "Animal:", animal)

print("\n*** III ***")
numbers = [1, 2, 3, 4, 5, 6, 7]
squares = [x * x for x in numbers if x % 2 == 0]
print(squares)
