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
        return self.diagonal

    def get_picture(self) :
        int_width = int(self.width)
        int_height = int(self.height)

        if int_height > 50 or int_width > 50 :
            return "Too big for picture."


        line_string = '*' * int_width + '\n'
        picture_string = line_string * int_height
        
        return picture_string


    def get_amount_inside(self, baby_rect) :
        fitting_widths = self.width / baby_rect.width
        fitting_heights = self.height / baby_rect.height

        if fitting_widths < 1 or fitting_heights < 1 :
            return 0
        else :
            return int(fitting_widths) * int(fitting_heights)

    def __str__(self) :
        return("Rectangle(width=" + str(int(self.width)) + ", height=" + str(int(self.height)) + ")")

class Square(Rectangle):
    def __init__(self, length):
        self.width = float(length)
        self.height = float(length)

    def __str__(self) :
        return("Square(side=" + str(int(self.width)) + ")")

    
    def set_side(self, length) :
        self.width = float(length)
        self.height = float(length)

    def set_height(self, length) :
        set_side(self, length)

    def set_length(self, length) :
        set_side(self, length)

    

# rect4 = Square(4)

# rect1 = Square(1)



# print(rect4.get_amount_inside(rect1))
