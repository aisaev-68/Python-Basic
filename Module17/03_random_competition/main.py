import random

first_command = list(round(random.uniform(5, 10), 2) for _ in range(20))
second_command = list(round(random.uniform(5, 10), 2) for _ in range(20))
champions = list((first_command[i] if first_command[i] > second_command[i] else second_command[i])
                 for i in range(len(first_command)))
print('Первая команда:', first_command, '\nВторая команда:', second_command,
      '\nПобедители тура:', champions)
