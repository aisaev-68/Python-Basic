import random


class People:
    # Это кол-во еди, деньги и дом
    food = 50
    money = 0
    house = True

    def __init__(self, name):
        self.name = name
        self.full_fed = 50  # Это сытость человека

    # функция сытости
    def full_feds(self):
        if self.full_fed < 20:
            self.eat()
        if self.full_fed < 0:
            self.print_death()

    # функция количества еды
    def foods(self):
        if People.food < 10:
            self.go_to_shop()

    # функция количества денег
    def moneys(self):
        if People.money < 50:
            self.working()

    # функция играть
    def play(self):
        self.full_fed -= 1

    # функция работать
    def working(self):
        # Работать (− сытость, + деньги).
        self.full_fed -= 1
        People.money += 1

    # функция есть
    def eat(self):
        People.food -= 1
        self.full_fed += 1

    # функция сходить в магазин
    def go_to_shop(self):
        People.food += 1
        People.money -= 1

    # функция генератор чисел кубика
    def generator_cube(self):
        numb = random.randint(1, 6)
        if numb == 1:
            self.working()
        elif numb == 2:
            self.eat()
        elif numb == 3:
            self.moneys()
        elif numb == 4:
            self.foods()
        elif numb == 5:
            self.full_feds()
        else:
            self.play()

    # функция печать смерти
    def print_death(self):
        print('{} умер от голода!'.format(self.name))

    def print_info(self):
        print('Сытость {} составляют {}'.format(self.name, self.full_fed))

    def get_state(self):
        return self.full_fed


people1 = People('Tom')
people2 = People('Bob')
for i in range(1, 366):
    print('\n-------день {}--------'.format(i))
    if people1.get_state() >= 0:
        people1.print_info()
        people1.generator_cube()
    else:
        print('{} умер от голода'.format(people1.name))
    if people2.get_state() >= 0:
        people2.print_info()
        people2.generator_cube()
    else:
        print('{} умер от голода'.format(people2.name))
    if people1.get_state() < 0 and people2.get_state() < 0:
        print('{} и {} умерли от голода на {} день'.format(people1.name, people2.name, i))
        break
