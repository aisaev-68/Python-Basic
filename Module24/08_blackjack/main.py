import random


class Card:
    def __init__(self):
        cards = ['Король', 'Дама', 'Валет', 'Туз', 2, 3, 4, 5, 6, 7, 8, 9, 10]
        suits = ['Пика', 'Червь', 'Бубна', 'Треф']
        self.list_card = [(str(i_cards) + ' ' + i_suits) for i_cards in cards for i_suits in suits]
        random.shuffle(self.list_card)

    def get_cards(self):
        return self.list_card.pop()


class Hand:

    def __init__(self, name):
        self.name = name
        self.lst_cards = []

    def add_cards(self, card):
        self.lst_cards.append(card)

    def points_game(self):
        res = 0
        for i_card in self.lst_cards:
            card = i_card.split()[0]
            if card.isalpha():
                if card == 'Туз':
                    if self.lst_cards.count(card) == 1:
                        res += 1
                    else:
                        res += 11
                else:
                    res += 10
            else:
                res += int(card)

        return res

    def __str__(self):
        txt = 'Карты {}:\n'.format(self.name)
        for card in self.lst_cards:
            txt += str(card) + ' '
        txt += "\nОчки: " + str(self.points_game())
        print('---------------------------')
        return txt


def compare_points(var1, var2, name1, name2):
    count = 0
    if var1 > 21:
        print('{} проиграл: {}:{}'.format(name1, var1, var2))
        count += 1
    elif var2 > 21:
        print('{} проиграл: {}:{}'.format(name2, var2, var1))
        count += 1

    if count != 0:
        return True
    return False


car = Card()
people = Hand('Tom')
computer = Hand('Computer')
people.add_cards(car.get_cards())
people.add_cards(car.get_cards())
print(people)
computer.add_cards(car.get_cards())
computer.add_cards(car.get_cards())
while people.points_game() <= 21:
    try:
        question = int(input('Будете брать карту? (1 - да, 2 - нет) '))
        if question == 1:
            people.add_cards(car.get_cards())
            print(people)
            if compare_points(people.points_game(), computer.points_game(), people.name, computer.name):
                break
        elif question == 2:
            if people.points_game() > computer.points_game():
                print('\nВыиграл {} со счетом {}:{}'.format(people.name, people.points_game(),
                                                            computer.points_game()))
            elif people.points_game() < computer.points_game():
                print('\nВыиграл {} со счетом {}:{}'.format(computer.name, computer.points_game(),
                                                            people.points_game()))
            else:
                print('\nНичья со счетом {}:{}'.format(computer.name, computer.points_game(),
                                                       people.points_game()))
            break
        else:
            raise TypeError
    except (ValueError, TypeError) as error:
        print('\nОшибка ввода! Введите 1 или 2.')
