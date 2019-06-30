class Parent():

    def __init__(self):
        print("Parent Init")

    def parent(self):
        print("Parent parent")

    def poke(self):
        print("Parent poked")


class Child(Parent):

    def __init__(self):
        print("Child Init przed")
        super().__init__()
        print("Child Init po")

    def poke(self):
        print("Child poked before")
        super().poke()
        print("Child poked after")

child = Child()
child.poke()