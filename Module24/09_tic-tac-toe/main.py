class Board:
    def __init__(self):
        self.fields = [i for i in range(9)]

    def update(self, seed, symb):
        self.fields[seed] = symb

    def print_board(self):
        i = 0
        for i_item in self.fields:
            if i % 3 == 0:
                print('\n-------------')
                print('|', i_item, end=' |')
            else:
                print('', i_item, end=' |')
            i += 1
        print('\n-------------')


class Players:

    def __init__(self, name, symb):
        self.name = name
        self.symb = symb

    def play(self):
        Board.update(self.symb)

    def check(self, board):
        coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for i_coord in coord:
            if board[i_coord[0]] == board[i_coord[1]] == board[i_coord[2]]:
                return self.name
        return False


game = Board()
game.print_board()
players1 = Players('Tom', 'X')
players2 = Players('Bob', 'O')

count = 0
while True:
    if count % 2 == 0:
        number = int(input('\n{} введите номер ячейки: '.format(players1.name)))
        game.update(number, players1.symb)
        buff = players1.check(game.fields)
    else:
        number = int(input('\n{} введите номер ячейки: '.format(players2.name)))
        game.update(number, players2.symb)
        buff = players2.check(game.fields)
    game.print_board()
    count += 1
    if count > 4:
        if buff:
            print('{} выиграл!'.format(buff))
            break
    if count == 9:
        print('Ничья!')
        break
