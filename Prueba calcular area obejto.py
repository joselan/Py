class Rectangle():

    def __init__(self, w, l):

        self.width = w

        self.length = l

   

    def calculate_perimeter(self):

        print( 2*(self.length + self.width))

   



class Square():

    def __init__(self, l):

        self.length = l

   

    def calculate_perimeter(self):

        print(4*self.length)



square = Square(10)

rect = Rectangle(2,5)

square.calculate_perimeter()

rect.calculate_perimeter()
