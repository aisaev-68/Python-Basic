import math


class Car:
    def __init__(self, x=0, y=0, angel=0):
        self.__x = x
        self.__y = y
        self.__angel = angel

    def move(self, distance):
        self.__x = round(self.__x + distance * math.sin(math.radians(self.__angel)))
        self.__y = round(self.__y + distance * math.cos(math.radians(self.__angel)))

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getAng(self):
        return self.__angel

    def setX(self, new_x):
        self.__x = new_x

    def setY(self, new_y):
        self.__y = new_y

    def setAng(self, new_angel):
        self.__angel = new_angel

    def __str__(self):
        if isinstance(self, Bus):
            var = 'Автобус'
        else:
            var = 'Автомобиль'
        return '\n{} тронулся из точки с координатами ({}, {}) в направлении {}.'.format(var, self.__x, self.__y,
                                                                                         self.__angel)


class Bus(Car):
    __tax_move = 100
    __number_seats_bus = 40

    def __init__(self, x, y, angel):
        super().__init__(x, y, angel)
        self.__passengers = 0
        self.__money = 0

    def move(self, distance):
        super(Bus, self).move(distance)
        print('Остановка на {} км.'.format(distance))

    def getMoney(self):
        return self.__money

    def enter(self, n):
        if self.__number_seats_bus >= self.__passengers + n:
            self.__passengers += n
            self.__money += self.__passengers * self.__tax_move
            print('Посадка {} пассажиров. Выручено {} денег.'.format(n, self.__money))
        elif self.__number_seats_bus < self.__passengers + n:
            self.__passengers = self.__number_seats_bus - self.__passengers
            self.__money += self.__passengers * self.__tax_move
            print('Посадка {} пассажиров. Выручено {} денег.'.format(self.__passengers, self.__money))

    def exit(self, n):
        if n >= 0:
            if n >= self.__passengers:
                self.__passengers = 0
        else:
            self.__passengers -= n
        print('Высадка {} пассажиров'.format(n))


bus1 = Bus(10, 15, 0)
print(bus1)
bus1.move(10)
bus1.enter(5)
print(bus1)
bus1.move(7)
bus1.enter(5)
bus1.setAng(45)
print(bus1)
bus1.move(7)
bus1.enter(3)
bus1.setAng(45)
bus1.exit(1)
print(bus1)
bus1.move(5)
bus1.exit(3)
print(bus1)
bus1.move(15)
bus1.enter(10)
bus1.exit(4)
bus1.setAng(60)
