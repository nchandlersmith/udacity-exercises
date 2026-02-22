from house import House, HouseBuilder


class TestHouse:
    def test_house(self):
        house = House()
        assert house is not None

    def test_house_builder(self):
        house_builder = HouseBuilder()
        result = house_builder.build()
        assert isinstance(result, House)

    def test_house_builder_adds_walls(self):
        house_builder = HouseBuilder()
        house = house_builder.set_walls("brick").build()
        assert house.walls == "brick"
        
    def test_house_builder_adds_roof(self):
        house_builder = HouseBuilder()
        house = house_builder.set_roof("shingles").build()
        assert house.roof == "shingles"