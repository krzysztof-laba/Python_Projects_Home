

"Zapis w pliku"
plik = open("Lista moja.txt", "w")
plik.write("ala ma kota\n333") # funkcja '\n' robi enter
plik.close()

"Odczyt z pliku"
plik = open("Lista moja.txt", "r")
variable = plik.readlines()
plik.close()
print(variable)