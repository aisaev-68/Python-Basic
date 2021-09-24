import random


class House:
    def __init__(self):
        self.__money = 100
        self.__food = 50
        self.__cat_food = 30
        self.__dirt = 0

    def getFood(self):
        return self.__food

    def getMoney(self):
        return self.__money

    def getCatFood(self):
        return self.__cat_food

    def getDirt(self):
        return self.__dirt

    def setMoney(self, mon):
        self.__money += mon

    def setFood(self, fd):
        self.__food += fd

    def setCatFood(self, cat_fd):
        self.__cat_food += cat_fd

    def setDirt(self, drt):
        self.__dirt += drt

    def __str__(self):
        return '\nЗапасы еды - {} единиц, \nзапасы кошачьего корма - {} единиц, ' \
               '\nбюджет семьи - {} единиц, \nгрязь - {} единиц.'.format(self.__food, self.__cat_food,
                                                                         self.__money, self.__dirt)


class Family:
    __total_furcoat = [0]
    __total_food = [0]
    __total_catfood = [0]
    __total_moneys = [0]

    def __init__(self):
        self.__satiety = 30
        self.__happiness = 100
        self.__death = False
        self.__house = home

    def setTotal_furcoat(self):
        Family.__total_furcoat[0] += 1

    def setTotal_food(self, fd):
        Family.__total_food[0] += fd

    def setTotal_catfood(self, catfd):
        Family.__total_catfood[0] += catfd

    def setTotal_moneys(self):
        Family.__total_moneys[0] += 150

    def setHappiness(self, happiness):
        self.__happiness += happiness

    def setSatiety(self, satiety):
        self.__satiety += satiety

    def getSatiety(self):
        return self.__satiety

    def getTotal_furcoat(self):
        return Family.__total_furcoat

    def getTotal_catfood(self):
        return Family.__total_catfood[0]

    def getHappiness(self):
        return self.__happiness

    def depress(self):
        if self.__house.getDirt() > 90:
            self.__happiness -= 10

    def print_info(self):
        print('\nЗа отчетный период заработано {} денег, \nсъедено людьми еды {}, ' \
              '\nсъедено домашними животными {}, \nкуплено шуб {}'.format(
            self.__total_moneys[0], abs(self.__total_food[0] - self.__house.getFood()),
            abs(self.__total_catfood[0] - self.__house.getCatFood()), self.__total_furcoat[0]))


class Husband(Family):
    def __init__(self, name):
        super().__init__()
        self.__name = name
        self.__house = home

    def __str__(self):
        return 'У {} сытость равна {}, счастье равна {} '.format(self.__name, self.getSatiety(), self.getHappiness())

    def actions(self):
        if self.getHappiness() < 10 or self.getSatiety() < 0:
            print("{} умер.".format(self.__name))
            return

        super().depress()
        if self.__house.getMoney() < 70:
            self.go_to_work()
        elif self.getHappiness() < 60:
            self.play()
        elif self.getHappiness() < 50:
            self.pet_cat()
        elif self.getSatiety() < 30:
            self.eat()
        else:
            self.go_to_work()

    def eat(self):
        if self.getSatiety() > 40:
            self.go_to_work()
        elif self.getSatiety() > 30:
            self.play()
        elif self.__house.getFood() < 30:
            self.go_to_work()
        elif self.__house.getFood() > 20:
            self.__house.setFood(-20)
            self.setSatiety(20)
            self.setTotal_food(20)
            print('{} от души поел'.format(self.__name))
        else:
            self.pet_cat()

    def pet_cat(self):
        if self.getSatiety() < 20:
            self.eat()
        else:
            self.setHappiness(5)
            self.setSatiety(-10)
            print('{} кота погладил.'.format(self.__name))

    def play(self):
        if self.getSatiety() < 20:
            self.eat()
        else:
            self.setHappiness(20)
            self.setSatiety(-10)
            print('{} поиграл на компьютере'.format(self.__name))

    def go_to_work(self):
        if self.getSatiety() < 30:
            self.eat()
        else:
            self.setSatiety(-10)
            self.__house.setMoney(150)
            self.setTotal_moneys()
            print('{} пошел на работу и заработал денег.'.format(self.__name))


class Wife(Family):
    def __init__(self, name):
        super().__init__()
        self.__name = name
        self.__house = home

    def __str__(self):
        return 'У {} сытость равна {}, счастье равна {} '.format(self.__name, self.getSatiety(), self.getHappiness())

    def actions(self):
        if self.getHappiness() < 10 or self.getSatiety() < 0:
            print("{} умерла.".format(self.__name))
            return

        super().depress()
        if self.__house.getFood() < 100:
            self.bay_food()
        if self.__house.getCatFood() < 20:
            self.bay_food()
        elif self.getHappiness() < 30:
            self.bay_fur_coat()
        elif self.getHappiness() < 20:
            self.pet_cat()
        elif self.getSatiety() < 30:
            self.eat()
        elif self.__house.getDirt() > 90:
            self.house_cleaning()
        else:
            self.bay_fur_coat()

    def eat(self):
        if self.getSatiety() > 40:
            self.pet_cat()
        elif self.__house.getFood() < 30:
            self.bay_food()
        elif self.__house.getFood() > 20:
            self.__house.setFood(-20)
            self.setSatiety(20)
            self.setTotal_food(20)
            print('{} от души поела'.format(self.__name))
        else:
            print('Еда кончилась! Надо сходить в магазин.')
            self.bay_food()

    def bay_food(self):
        if self.__house.getMoney() >= 400:
            self.__house.setFood(120)
            self.setTotal_food(120)
            self.__house.setCatFood(40)
            self.setTotal_catfood(40)
            self.__house.setMoney(-160)
            self.setSatiety(-10)
            print('{} купила продукты'.format(self.__name))
        elif self.__house.getMoney() >= 80:
            self.__house.setFood(60)
            self.setTotal_food(60)
            self.__house.setCatFood(20)
            self.setTotal_catfood(20)
            self.__house.setMoney(-80)
            self.setSatiety(-10)
            print('{} купила продукты'.format(self.__name))
        else:
            self.pet_cat()

    def bay_fur_coat(self):
        if self.__house.getMoney() > 700:
            if self.getTotal_furcoat()[0] <= 10:
                self.__house.setMoney(-350)
                self.setHappiness(60)
                self.setTotal_furcoat()
                self.setSatiety(-10)
                print('Какое счастье! Наконец-то купила шубу.')
            else:
                self.bay_food()
        else:
            self.pet_cat()

    def house_cleaning(self):
        if self.__house.getDirt() > 90:
            self.__house.setDirt(-100)
            self.setHappiness(-10)
            self.setSatiety(-10)
            print('Уборка дома завершена.')
        else:
            self.eat()

    def pet_cat(self):
        if self.getSatiety() < 20:
            self.eat()
        else:
            self.setHappiness(5)
            self.setSatiety(-10)
            print('{} кота погладил (а).'.format(self.__name))


class Child(Family):
    def __init__(self, name):
        super().__init__()
        self.__name = name
        self.__house = home

    def __str__(self):
        return 'У {} сытость равна {}, счастье равна {} '.format(self.__name, self.getSatiety(), self.getHappiness())

    def actions(self):
        if self.getHappiness() < 10 or self.getSatiety() < 0:
            print("{} умер от голода.".format(self.__name))
            return
        super().depress()
        rand = random.randint(1, 3)
        if self.getSatiety() < 30:
            self.eat()
        elif rand == 1:
            self.cry()
        elif rand == 2:
            self.eat()
        elif rand == 3:
            self.eat()
        else:
            self.sleep()

    def cry(self):
        print('{} весь день плачеть.'.format(self.__name))
        self.setHappiness(-20)

    def sleep(self):
        print('{}  спал весь день.'.format(self.__name))
        self.setSatiety(-20)

    def eat(self):
        self.__house.setFood(-20)
        self.setSatiety(20)
        self.setHappiness(20)
        self.setTotal_food(20)
        print('{} поел.'.format(self.__name))


class Cat(Family):
    def __init__(self, name):
        super().__init__()
        self.__name = name
        self.__satiety = 30
        self.__house = home

    def __str__(self):
        return 'У кота {} сытость равна {}'.format(self.__name, self.__satiety)

    def actions(self):
        if self.__satiety < 0:
            print('Кот {} умер от голода.'.format(self.__name))
            return
        rand = random.randint(1, 3)
        if self.__satiety < 30:
            self.eat()
        elif rand == 1:
            self.sleep()
        elif rand == 2:
            self.tearwallpaper()
        elif rand == 4:
            self.eat()

    def eat(self):
        if self.__house.getCatFood() > 20:
            self.__house.setCatFood(-10)
            self.setTotal_catfood(10)
            self.__satiety += 20
            print('Кот {} поел.'.format(self.__name))
        else:
            self.tearwallpaper()

    def tearwallpaper(self):
        self.__house.setDirt(5)
        self.__satiety -= 10
        print('Кот {} содрал обои.'.format(self.__name))

    def sleep(self):
        print('Кот {} спал целый день.'.format(self.__name))
        self.__satiety -= 10


home = House()
husband = Husband('Иван')
wife = Wife('Татьяна')
child = Child('Гришка')
cat1 = Cat('Борис')
cat2 = Cat('Кис')
print(husband)
for day in range(1, 366):
    print('\n------------{}-й день--------------'.format(day))
    home.setDirt(5)
    husband.actions()
    wife.actions()
    child.actions()
    cat1.actions()
    cat2.actions()
    print(husband)
    print(wife)
    print(child)
    print(cat1)
    print(cat2)
print(home)
husband.print_info()
