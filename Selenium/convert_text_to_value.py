""" Przekonwertowanie tekstu na liczbę którą można użyć np w warunku 'if' """
wartosc_pln = '7 000 PLN'


wartosc_pln_no_spaces = wartosc_pln.replace(" ","").replace("PLN","")
print(wartosc_pln_no_spaces)

wartosc_2 = 500

dodawanie = int(wartosc_pln_no_spaces) + wartosc_2
print(dodawanie)

if dodawanie <= 8000:
	print("Wartość mniejsza, równa 8000")
else:
	print("Wartość OK!")