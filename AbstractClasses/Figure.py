from abc import ABC, abstractmethod
from math import pi
from AbstractClasses.Colors import Colors


class Figure(ABC):

    @abstractmethod  # Abstract method
    def get_name(self):
        print("No name of class Figure.")
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
        return "Square"

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def get_name(self):
        return "Circle"

    def area(self):
        return self.radius * self.radius * pi

    def perimeter(self):
        return 2 * pi * self.radius


class Parallelogram(Figure):
    def __init__(self, side_a, side_b, angle):
        self.side_a = side_a
        self.side_b = side_b
        self.angle = angle

    def get_name(self):
        return "Parallelogram"

    def area(self):
        return self.side_a * self.side_b * self.angle

    def perimeter(self):
        return self.side_a + self.side_b * 2


class CustomFormatter(object):

    @staticmethod  # Static method is used when does not create instance of the class.
    def format_figure(figure_name, figure_value):
        value_format = round(figure_value, 1)
        output_string = "Area for {0} is: {1}".format(figure_name, value_format)
        return output_string


#######################################################################################################################
class TestRunner(object):
    list = []

    def add_figure(self, figure_test_class):
        self.list.append(figure_test_class)
        return

    def run_tests(self):
        for figure_test_class in self.list:
            print(CustomFormatter.format_figure(figure_test_class.get_name(), figure_test_class.area()))


print(Colors.fg.blue, "\n********************************************************************************")
print("I. First method how to display figures parameters.")
test_runner = TestRunner()
test_runner.add_figure(Square(3.33))  # Square object.
test_runner.add_figure(Circle(5))  # Circle object.
test_runner.add_figure(Parallelogram(4, 5, 1))
test_runner.run_tests()  # Display figures some parameters (name and area).
print(Colors.reset)


print(Colors.fg.green, "\n********************************************************************************")
print("II. SECOND METHOD HOW TO DISPLAY FIGURES PARAMETERS:")
square = Square(5.3)  # Create Square object.
circle = Circle(5)  # Create Circle object.
list_2 = []  # Create empty list of objects.
list_2.append(square)  # Append objects.
list_2.append(circle)  # Append objects.

print(Colors.fg.purple, "\nOnly display figure name and area - without formatting.")
for figure in list_2:
    print("{0} area: {1}".format(figure.get_name(), figure.area()))

print(Colors.fg.cyan, "\nDisplay with formatting.")
for figure in list_2:
    print(CustomFormatter.format_figure(figure.get_name(), figure.area()))
