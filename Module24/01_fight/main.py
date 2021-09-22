import random


class Units:

    def __init__(self, name_warrior):
        self.name = name_warrior
        self.health = [100]
        print('Создан воин {} со здоровьем {}'.format(self.name, self.health[0]))

    def strike(self, warrior):
        print('\nВоин {} нанес удар воину {}'.format(self.name, warrior.name))
        warrior.health[0] -= 20
        warrior.health_status()

    def health_status(self):
        print('У воина {} осталось {} здоровья'.format(self.name, self.health[0]))


first_warrior = Units('Путин')
second_warrior = Units('Байден')
n_round = 0
name = rival_name = ''

while first_warrior.health[0] > 0 and second_warrior.health[0] > 0:
    n_round = random.randint(1, 2)
    if n_round == 1:
        first_warrior.strike(second_warrior)
    elif n_round == 2:
        second_warrior.strike(first_warrior)

if n_round == 1:
    name = first_warrior.name
    rival_name = second_warrior.name
elif n_round == 2:
    name = second_warrior.name
    rival_name = first_warrior.name

print('\nВыиграл воин {}, одержав победу над воином {}'.format(name, rival_name))
