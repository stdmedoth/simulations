from vectors import Vector

class Velocity :
    def __init__(self, position) -> None:
        self.vector = Vector(position)

    def get_vector(self):
        return self.vector