import time


class TrafficLight:
    __color = 'КРАСНЫЙ'

    def running(self):
        print('Светофор работает')

        self.__color = 'КРАСНЫЙ'
        print(f'Загорелся: {self.__color}')
        time.sleep(7)

        self.__color = 'ЖЕЛТЫЙ'
        print(f'Загорелся: {self.__color}')
        time.sleep(2)

        self.__color = 'ЗЕЛЕНЫЙ'
        print(f'Загорелся: {self.__color}')
        time.sleep(5)

        while True:
            self.running()


traff_light = TrafficLight()
print(traff_light.running())



