class Property:
    def __init__(self, typ_property, worth):
        self.type_property = typ_property
        self.worth = worth
        self.money = 0

    def tax_calc(self):
        return 0

    def __str__(self):
        return '\nНалог составляет {} рублей. Деньги хватают для оплаты налога.'.format(self.tax_calc()) if float(
            self.money) > self.tax_calc() else '\nНалог составляет {} рублей. ' \
                                               'Для оплаты налога не хватает {} рублей.'.format(
            self.tax_calc(), abs(float(self.money) - self.tax_calc())
        )


class Apartment(Property):
    def __init__(self, typ_property, worth, money):
        super().__init__(typ_property, worth)
        self.money = money

    def tax_calc(self):
        return round(self.worth / 1000, 2)


class Car(Property):
    def __init__(self, typ_property, worth, money):
        super().__init__(typ_property, worth)
        self.money = money

    def tax_calc(self):
        return round(self.worth / 200, 2)


class CountryHouse(Property):
    def __init__(self, typ_property, worth, money):
        super().__init__(typ_property, worth)
        self.money = money

    def tax_calc(self):
        return round(self.worth / 500, 2)


try:
    type_property = input('Введите вид имущества (квартира, автомобиль, дача): ').lower()
    my_money = float(input('Введите количество денег: '))
    my_price = float(input('Введите стоимость имущества: '))
    if type_property == 'квартира':
        my_apartment = Apartment('квартира', my_price, my_money)
        print(my_apartment)
    elif type_property == 'автомобиль':
        my_car = Car('автомобиль', my_price, my_money)
        print(my_car)
    elif type_property == 'дача':
        my_countryhouse = CountryHouse('дача', my_price, my_money)
        print(my_countryhouse)
    else:
        raise ValueError
except ValueError:
    print('Ошибка ввода!')
