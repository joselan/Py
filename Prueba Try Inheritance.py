class Shape():
    def what_am_i(self):
        print("I am a shape")
 
 
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
 
    def calculate_perimeter(self):
        return 2 * self.width + 2 * self.length
 
 
class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1
 
    def calculate_perimeter(self):
        return self.s1 * 4
 
    def change_size(self, x):
        self.s1 += x
        return self.s1
 
 
    
a_rec = Rectangle(4,8)
 
a_squ = Square(3)
 
print(a_rec.calculate_perimeter()) 
print(a_squ.calculate_perimeter()) 

a_squ.what_am_i()
a_rec.what_am_i()
