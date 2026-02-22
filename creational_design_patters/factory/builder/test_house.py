from house import House, HouseBuilder


class TestHouseBuilder:
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

    def test_house_builder_adds_windows(self):
        house_builder = HouseBuilder()
        house = house_builder.set_windows("double pane").build()
        assert house.windows == "double pane"

    def test_house_builder_adds_doors(self):
        house_builder = HouseBuilder()
        house = house_builder.set_doors("wooden").build()
        assert house.doors == "wooden"

    def test_house_builder_adds_garage(self):
        house_builder = HouseBuilder()
        house = house_builder.set_garage("two car").build()
        assert house.garage == "two car"
