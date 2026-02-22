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
