import random


class Karma:
    __total_ball = [0]

    def __init__(self, max_ball):
        self.__max_ball = max_ball
        self.__list_except = ['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError']
        self.__new_file = open('karma.log', 'w', encoding='utf-8')

    def one_day(self):
        random.shuffle(self.__list_except)
        try:
            if random.randint(1, 10) == 7:
                raise Exception
            self.__total_ball[0] += random.randint(1, 7)
        except Exception:
            self.write_file(self.__list_except[0])
        return self.__total_ball[0]

    def write_file(self, logtxt):
        self.__new_file.write(logtxt + '\n')

    def __str__(self):
        return f'Вы набрали {self.__total_ball[0]} очков.'


max_bal = 500
my_karma = Karma(500)
day_count = 0
while True:
    day_count += 1
    if int(my_karma.one_day()) <= max_bal:
        print(f'\n------------{day_count}-й день-------------')
        print(my_karma)
    else:
        break
