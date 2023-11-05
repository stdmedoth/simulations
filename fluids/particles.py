from vectors import Vector 
from velocity import Velocity

class Particle :
    def __init__(self, position, velocity) -> None:
        self.vector = Vector(position)
        self.velocity = Velocity(velocity)
    
    def get_velocity(self):
        return self.velocity

    def set_position(self, position):
        return self.vector.set_position(position)

    def get_position(self):
        return self.vector.get_position()