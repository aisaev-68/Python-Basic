# класс картошка
class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    # метод роста
    def grow(self):
        if self.state < 3:
            self.state += 1
            self.print_state()

    # рост картошки
    def is_ripe(self):
        if self.state == 3:
            return True
        else:
            return False

    # информация зрелости
    def print_state(self):
        print('Картоша {} сейчас {}'.format(self.index, Potato.states[self.state]))


# класс грядка
class PotatoGarden:

    # список картошки
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    # рост грядки
    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    # созревание картошки
    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка еще не созрела!\n')
            return False
        else:
            print('Вся картошка созрела! Можно собирать!')
            return True

    def get(self):
        return len(self.potatoes)


class Gardener:
    works_garden = {0: 'отсутствует', 1: 'окучивает грядку', 2: 'поливает грядку', 3: 'собирает картошку'}

    def __init__(self, name, garden):
        self.name = name
        self.garden = garden
        self.work_garden = 0

    def progress_work(self):
        if self.work_garden < 3:
            self.work_garden += 1
        self.print_work_garden()

    def i_work_garden(self):
        for i_garden in self.garden:
            i_garden.progress_work()

    def print_work_garden(self):
        print('Садовник {}  сейчас {}'.format(self.name, Gardener.works_garden[self.work_garden]))

    def gardener_works(self):
        if self.garden.are_all_ripe():
            potatoes = self.garden.get()
            print('Собрано картошки {} штук'.format(potatoes))


my_garden = PotatoGarden(3)
my_garden.are_all_ripe()
gardener = Gardener('Максим', my_garden)
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()
    gardener.progress_work()
    gardener.gardener_works()
