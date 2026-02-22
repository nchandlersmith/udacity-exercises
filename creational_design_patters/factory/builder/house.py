"""House for builder pattern example."""

class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.windows = None
        self.doors = None
        self.garage = None
        
        
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