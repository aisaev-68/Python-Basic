# Класс вода steam - пар, storm - шторм, dirt - грязь, lava - лава, lightning - молния, dust - пыль
class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        else:
            return None


# Клас огонь
class Fire:

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        else:
            return None


# Класс воздух
class Air:

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


# Класс земля(в смысле глина)
class Earth:

    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None


class Dirt:
    def __str__(self):
        return 'Грязь'


class Dust:
    def __str__(self):
        return 'Пыль'


class Lava:
    def __str__(self):
        return 'Лава'


class Lightning:
    def __str__(self):
        return 'Молния'


class Storm:
    def __str__(self):
        return 'Шторм'


class Steam:
    def __str__(self):
        return 'Пар'


a = Air()
b = Water()
c = a + b
print('{} + {} = {}'.format(a, b, c))
