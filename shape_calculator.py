class Rectangle:
    
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)


    def set_width(self, width) :
        self.width = float(width)

    def set_height(self, height) :
        self.height = float(height)

    def get_area(self) :
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self) :
        self.perimeter = 2 * (self.height + self.width)
        return self.perimeter

    def get_diagonal(self) :
        self.diagonal = (self.width ** 2 + self.height ** 2)**.5

    def get_picture(self) :
        int_width = int(self.width)
        int_height = int(self.height)

        if int_height > 50 or int_width > 50 :
            return "Too big for picture."


        line_string = '*' * int_width + '\n'
        picture_string = line_string * int_height
        
        return picture_string


    def get_amount_inside(self) :
        pass

    def __str__(self) :
        pass

class Square:
    pass

rect = Rectangle(4, 14)

print(rect.get_picture())