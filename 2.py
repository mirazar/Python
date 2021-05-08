class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        mass_on_m2 = 25
        thickness = 5
        mass = self._width * self._length * mass_on_m2 * thickness
        return mass


road = Road(20, 5000)
print(road.asphalt_mass())
