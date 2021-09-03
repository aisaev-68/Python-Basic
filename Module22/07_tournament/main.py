def print_contents(f_file):
    with open(f_file, 'r', encoding='utf-8') as d_file:
        print(f'\nСодержимое файла {f_file}:')
        for i_elem in d_file.readlines():
            print(i_elem, end='')
        print()


count = 0
with open('first_tour.txt', 'r', encoding='utf-8') as file:
    print_contents(file.name)
    lines_first_tour = file.readlines()
    file.seek(0, 0)
    ball = int(file.readline())
    with open('second_tour.txt', 'w', encoding='utf-8') as new_file:
        new_file.writelines('\n')
        for i_line in range(len(lines_first_tour) - 1, 0, -1):
            surname, name, balls = lines_first_tour[i_line].split()
            if ball < int(balls):
                count += 1
                new_file.writelines(f'{count}) {name[:1]}. {surname} {str(balls)}\n')
        new_file.seek(0, 0)
        new_file.writelines(f'{str(count)}')
print_contents(new_file.name)
