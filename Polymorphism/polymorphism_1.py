class Wolf(object):
    def bark(self):
        print("hooooowll")

class Dog(object):
    def bark(self):
        print("woof")

class Cat(object):
    def bark(self):
        print("miauuuu")




def barkforme(dogtype): # przekazujemy obiekt dogtype (my_dog/my_wolf/my_cat) i po '.' robimy operacje.
    print("")
    dogtype.bark()



my_wolf = Wolf()
my_dog = Dog()
my_cat = Cat()


barkforme(my_dog)
barkforme(my_wolf)
barkforme(my_cat)

