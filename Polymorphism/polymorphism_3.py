class Document():
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method.")

class Pdf(Document):
    def show(self):
        return "Show pdf documents!"

class Word(Document):
    def show(self):
        return "Show word documents!"

documents = [Pdf('Document_1'), Pdf('Document_2'), Word('Document_3')]


for document in documents:
    print(document.name + ' : ' + document.show())





print("")
print("*** How inheritance works. ***", end="\n\n")

class Base_class():
    def __init__(self, name):
        self.name = name
        print("__init_ in base class. Name: '{0}'.".format(self.name))

    def test(self):
        raise NotImplementedError("Abstract class.")

class Another_class(Base_class):
    def test(self):
        self.show_inheritance()
        self.show_inheritance_2()

    def show_inheritance(self):
        print("inheritance from method 1")

    def show_inheritance_2(self):
        print("inheritance_2 from method 2")



another_class = Another_class("1-st class")
another_class.test()
print("")
another_class_2 = Another_class("2-nd class")
another_class_2.test()