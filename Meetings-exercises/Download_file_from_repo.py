class Make_Dictionary():
	viewE_builds = open("C:\PyCharm\PycharmProjects\lerning\Meetings\SharePoint-builds.txt", "r") # Otwieramy plik 'txt' ze wskazanej lokacji.
	dictionary_builds = {} # Tworzymy pusty słownik (dictionary) build'ów.
	dictionary_names = {} # Tworzymy pusty słownik (dictionary) z nazwami danego build'a.
	dictionary = {} # Tworzymy pusty słownik (dictionary) z nazwami danego build'a oraz z jego nazwą.
	i = 1 # Inicjujemy wartość początkową do słownika. Zamiast nazw build'a przypisujemy liczbę.
	for line in viewE_builds: # Dla każdej lini z odczytanego pliku wykonujemy w pętli for.
		split_1 = ">" # Separator - ma pomóc w parsowaniu danych.
		split_2 = "<" # Separator - ma pomóc w parsowaniu danych.
		y = line.split(split_2)[1].split(split_1)[0] # Separuje nazwy build'ów.
		dictionary_names[i] = y # Budowa słownika z nazwami build'ów.
		x = line.split(split_1)[1].split(split_2)[0]  # Separujemy numery build'ów.
		dictionary_builds[i] = x  # Budowa słownika a dokładnie jego wartości którym są nr build'ów.
		dictionary[y] = x # Budowa słownika (dictionary) z z nazwą build'a i numerem build'a.
		i += 1

	# print("Dictionary Name:", dictionary_names) # Słownik z nazwami build'ów wraz przypisaną nową numeracją.
	# print("Dictionary Builds:", dictionary_builds) # Słownik z nową numeracją i jej odpowiadające numery build'ów.
	# print("Dictionary:", dictionary) # Wypisanie słownika z nazwami i numerami build'ów.
	# print(dictionary.keys()) # Wypisanie kluczy z dictionary - [key : value]
	# print(dictionary.values()) # Wypisanie wartości z dictionary - [key : value]
	# print(dictionary_names[1])
	# print(dictionary["Product Version"])

print("Numery buildow:")
for i in Make_Dictionary.dictionary_builds:
	print(Make_Dictionary.dictionary_builds[i])
print("")
print("Nazwy buildow:")
for i in Make_Dictionary.dictionary_names:
	print(Make_Dictionary.dictionary_names[i])



# files_directories_path = {
# 	"ViewE_Image" : r"\\usmayvfile001\cvb\ViewE\Replicated\Packages\vieweimage",
# 	"Control_Flash_Kits" : r"\\usmayvfile001\cvb\ViewE\Replicated\Packages\viewe-system",
# 	"Rescue_Image" : r"\\usmayvfile001\cvb\ViewE\Replicated\Packages\viewe-system-rescue",
# 	"Logix_Designer" : r"",
# 	"Logix_FW" : r"",
# 	"View_Platform_srx" : r"\\usmayvfile001\cvb\ViewE\Replicated\Packages\viewe_platform_srx_wrl_usbtools",
# 	"View_Platform_wrl" : r"\\usmayvfile001\cvb\ViewE\Replicated\Packages\viewe_platform_extended_wrl_usbtools",
# 	"FTSP" : r"",
# 	"FTA" : r"",
# 	"RSLinx" = r""
#						}

