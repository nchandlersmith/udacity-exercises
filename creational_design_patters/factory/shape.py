class Shape:
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"


class Square(Shape):
    def draw(self):
        return "Drawing a Square"
    
    
class Triangle(Shape):
    def draw(self):
        return "Drawing a Triangle"

class ShapeFactory:
    @staticmethod
    def create(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        elif shape_type == "triangle":
            return Triangle()