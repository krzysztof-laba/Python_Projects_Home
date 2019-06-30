class Colors():
    """
    CLASS FROM INTERNET - I AM NOT AN OWNER.
    """
    '''Colors class:reset all colors with colors.reset; two
        sub classes fg for foreground
        and bg for background; use as colors.subclass.colorname.
        i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
        underline, reverse, strike through,
        and invisible work with the main class i.e. colors.bold'''
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'


class Wolf(object):
    def charakter(self):
        print("Wolf charakteres:")
    def color_set(self):
        print(Colors.fg.red)
    def color_reset(self):
        print(Colors.reset, end="")
    def bark(self):
        print("hooooowll")
    def sleeping(self):
        print("Sleep outside.")
    def eating(self):
        print("It is hunting.")

    def animal_type(self):
        print("Wolf is danger!!")

class Dog(object):
    def charakter(self):
        print("Dog charakters:")
    def color_set(self):
        print(Colors.fg.blue)
    def color_reset(self):
        print(Colors.reset, end="")
    def bark(self):
        print("woof")
    def sleeping(self):
        print("Sleep in a doghouse.")
    def eating(self):
        print("It is fed.")

    def animal_type(self):
        print("Dog defends the house!!")

class Cat(object):
    def charakter(self):
        print("Cat charakters:")
    def color_set(self):
        print(Colors.fg.darkgrey)
    def color_reset(self):
        print(Colors.reset, end="")
    def bark(self):
        print("miauuuu")
    def sleeping(self):
        print("Sleep near the stove.")
    def eating(self):
        print("It is fed.")

    def animal_type(self):
        print("Cat is lazy!!")



def barkforme(dogtype):
    dogtype.color_set()
    dogtype.charakter()
    dogtype.bark()
    dogtype.sleeping()
    dogtype.eating()
    dogtype.color_reset()

def animalType(tape_of_animal):
    print(Colors.fg.green, end="    ")
    tape_of_animal.animal_type()
    print(Colors.reset, end="")


my_wolf = Wolf()
my_dog = Dog()
my_cat = Cat()


barkforme(my_dog)
barkforme(my_wolf)
barkforme(my_cat)
print("")
animalType(my_wolf)
animalType(my_dog)
animalType(my_cat)