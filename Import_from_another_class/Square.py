import time
class Square(object):

    def __init__(self, a_length, b_length):
        self.aLength = a_length
        self.bLength = b_length

    def calculateArea(self):
        P = self.aLength * self.bLength
        # print(P)
        return P
        time.sleep(5)




# square = Square(4, 7)
# print("Square field, P = ", square.calculateArea())