from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = 'красный'

    def running(self):
        while True:
            if self.__color == 'красный':
                print('красный')
                sleep(7)
                self.__color = 'желтый'
            elif self.__color == 'желтый':
                print('желтый')
                sleep(2)
                self.__color = 'зеленый'
            else:
                print('зеленый')
                sleep(6)
                self.__color = 'красный'


light = TrafficLight()
light.running()
