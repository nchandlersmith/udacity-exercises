import pytest
from shape import ShapeFactory


class TestShape:

    @pytest.fixture
    def shape_factory(self):
        return ShapeFactory()

    def test_circle_draw(self, shape_factory):
        circle = shape_factory.create("circle")
        assert circle.draw() == "Drawing a Circle"

    def test_square_draw(self, shape_factory):
        square = shape_factory.create("square")
        assert square.draw() == "Drawing a Square"

    def test_triangle_draw(self, shape_factory):
        triangle = shape_factory.create("triangle")
        assert triangle.draw() == "Drawing a Triangle"
        
    def test_invalid_shape(self, shape_factory):
        with pytest.raises(AttributeError, match="Shape type pentagon is not supported"):
            shape_factory.create("pentagon")
