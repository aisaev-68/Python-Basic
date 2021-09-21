class Parent:

    def __init__(self, name, age, list_child=None):
        if list_child is None:
            list_child = []
        self.name = name
        self.age = age
        self.list_child = list_child

    def add_child(self, list_ch):
        for i_ch in list_ch:
            name_child, age_child = i_ch.split()
            if self.age - int(age_child) > 16:
                self.list_child.append(Child(name_child, int(age_child)))
            else:
                print('Возраст ребенка должен быть меньше возраста родителя хотя бы на 16 лет\n')

    def info_parent(self):
        print('Меня зовут {},мне {} лет. Список моих детей:\n'.format(
            self.name, self.age), end='')
        for i_ch in self.list_child:
            print('{}'.format('{} - {} лет. '.format(i_ch.name, i_ch.age)), end='')
        print('\n')

    def info_states(self):
        for i_ch in self.list_child:
            i_ch.info_child()

    def calm_the_child(self):
        for i_ch in self.list_child:
            if not i_ch.calm:
                i_ch.calm = True
            else:
                i_ch.calm = False

    def feed_the_child(self):
        for i_ch in self.list_child:
            if not i_ch.hunger:
                i_ch.hunger = True
            else:
                i_ch.hunger = False


class Child:

    def __init__(self, name, age, hunger=False, calm=False):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.calm = calm

    def info_child(self):
        print(
            'Имя: {}\nВозраст: {}\nГолоден: {}\nСпокоен: {}\n'.format(
                self.name, self.age, self.hunger, self.calm
            )
        )


par = Parent('Bob', 30)
par.add_child(['Tom 2', 'John 8'])
par.info_parent()
for i_time in range(24):
    print('---------{} час -----------'.format(i_time))
    par.info_states()
    par.calm_the_child()
