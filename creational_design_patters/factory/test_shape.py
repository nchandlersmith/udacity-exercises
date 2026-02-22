import pytest
from shape import ShapeFactory


class TestShape:

    def test_circle_draw(self, shape_factory):
        circle = ShapeFactory.create("circle")
        assert circle.draw() == "Drawing a Circle"

    def test_square_draw(self):
        square = ShapeFactory.create("square")
        assert square.draw() == "Drawing a Square"

    def test_triangle_draw(self):
        triangle = ShapeFactory.create("triangle")
        assert triangle.draw() == "Drawing a Triangle"
        
    def test_invalid_shape(self):
        with pytest.raises(AttributeError, match="Shape type pentagon is not supported"):
            ShapeFactory.create("pentagon")
