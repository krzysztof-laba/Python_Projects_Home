class Animal(object):
    def __init__(self, name, age, hungry):
        print("Innit")
        self.name = name
        self.age = age
        self.is_hungry = hungry


zebra = Animal("Jeffrey", 10, "Yes")
print(zebra.name, zebra.age, zebra.is_hungry)

giraffe = Animal("Bruce", 5, "True")
print(giraffe.name, giraffe.age, giraffe.is_hungry)

panda = Animal("Chad", 1, False)
# print(panda.__str__(), panda.name, panda.age, panda.is_hungry)

