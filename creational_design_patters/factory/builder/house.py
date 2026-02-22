"""House for builder pattern example."""


class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.windows = None
        self.doors = None
        self.garage = None
        self.pool = None

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build(self):
        return self.house

    def set_walls(self, walls):
        self.house.walls = walls
        return self

    def set_roof(self, roof):
        self.house.roof = roof
        return self

    def set_windows(self, windows):
        self.house.windows = windows
        return self

    def set_doors(self, doors):
        self.house.doors = doors
        return self

    def set_garage(self, garage):
        self.house.garage = garage
        return self
    
    def set_pool(self, pool):
        self.house.pool = pool
        return self


class HouseDirector:
    def __init__(self):
        self.builder = HouseBuilder()
        
    def create_standard_house(self):
        return self.builder \
            .set_walls("vinyl siding") \
            .set_roof("shingles") \
            .set_windows("double pane") \
            .set_doors("wooden") \
            .set_garage("single car") \
            .build()
            
    def create_luxury_house(self):
        return self.builder \
            .set_walls("stone") \
            .set_roof("tile") \
            .set_windows("triple pane") \
            .set_doors("steel") \
            .set_garage("three car") \
            .set_pool("in-ground") \
            .build()
