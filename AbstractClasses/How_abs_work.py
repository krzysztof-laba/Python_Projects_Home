from abc import ABC, abstractmethod


# Abstract class. Unable to create instance of the class.
# Easy to implement class like 'Square'.
# Figure inherits from ABS - abstract class.
class Figure(ABC):

    # Abstract method are base for creation next method in different classes.
    @abstractmethod  # Abstract method
    def get_name(self):
        pass

    @abstractmethod  # Abstract method
    def area(self): pass

    @abstractmethod  # Abstract method
    def perimeter(self):
        raise NotImplementedError
        # Returns exception when trying to make instance of Figure and call method perimeter.
        # And is not declare as @abstractmethod.


class Square(Figure):
    def __init__(self, side):
        self.side = side

    def get_name(self):
        return "Square"  # inherit from Figure (abstract class)."

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


giraffe = Figure()  # It is not allowed to create instance of the class 'Figure' because of ABS in Figure.
giraffe.get_name()  # Can not use method from abstract class.

# How polymorphism work:
list_of_elements = []
list_of_elements.append(Square(5))
for el in list_of_elements:
    print(el.area(), el.get_name(), el.perimeter())