

class Zwierze():

    def __init__(self, imie = "Reks", gatunek = "Pies", wiek = 5):
        self.name = imie
        self.type = gatunek
        self.age = wiek

    def dodaj_zwierze(self):
        imie = input("Podaj imie: ")
        gatunek = input("Podaj gatunek: ")
        wiek = input("Podaj wiek: ")
        if imie != "":
            self.name = imie

        if gatunek != "":
            self.type = gatunek
        if wiek != "":
            self.age = wiek

    def daj_glos(self):
        if self.type.lower() == "kot": # konwert wszystko na małe litery
            print("{} o imieniu {} ma {} lata i wydaje dźwięk '{}'".format(self.type, self.name, self.age, "Miauuu!!"))
        elif self.type == "Koza" or self.type == "koza":
            print("{} o imieniu {} ma {} lata i wydaje dźwięk '{}'".format(self.type, self.name, self.age, "Beeee!!"))
        elif self.type == "Krowa" or self.type == "krowa":
            print("{} o imieniu {} ma {} lata i wydaje dźwięk '{}'".format(self.type, self.name, self.age, "Muuuu!!"))
        elif self.type == "Pies":
            print("{} o imieniu {} ma {} lata i wydaje dźwięk '{}'".format(self.type, self.name, self.age, "HauHau!!"))
        else:
            print("Nie podałeś gatunku zwierzęcia")

zwierze = Zwierze()
zwierze.dodaj_zwierze()
zwierze.daj_glos()

