class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'машина {self.name} поехала!')

    def stop(self):
        print(f'машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'скорость {self.name} {self.speed} км ч')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение скорости')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение скорости')


class PoliceCar(Car):
    def __init__(self, *args):
        police_args = list(args[:3])
        police_args.append(True)
        super().__init__(*police_args)


car = TownCar(100, 'черный', 'ZAZ')

car.go()
car.turn('на право')
car.stop()
car.show_speed()
