class Vector:
    def __init__(self, position) -> None:
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
    
    def set_position(self, position):
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
    

    def get_position(self):
        return (self.x, self.y, self.z)
    
    def __str__(self) -> str:
        return "(%d, %d, %d)"%(self.x, self.y, self.z)
    