def f_size_list(lst, txt, txt1, txt2):
    i = 0
    n_count = int(input(txt))
    if n_count > 0:
        while i < n_count:
            print(txt1, i + 1, txt2, end='')
            numb = int(input())
            if numb > 0:
                lst.append(numb)
            else:
                print('\nОшибка ввода! Повторите ввод!\n')
                i -= 1
            i += 1
        print('')
    else:
        print('\nОшибка ввода! Повторите ввод!\n')
        f_size_list(lst, txt, txt1, txt2)
    lst.sort()
#    return lst


def people_size(f_lst, s_lst):
    n_count = 0
    p_count = 0
    for item in s_lst:
        for elem in f_lst:
            if int(elem) - int(item) >= 0:
                f_lst.remove(elem)
                n_count += 1
                break
        if n_count == 1:
            p_count += 1
            n_count = 0
    return p_count


txt1_input = 'Кол-во коньков: '
txt2_input = 'Кол-во людей: '
size_text = 'Размер'
shoes_text = 'пары: '
foot_text = 'Размер ноги'
people_text = 'человека: '
f_list = []
s_list = []
f_size_list(f_list, txt1_input, size_text, shoes_text)
f_size_list(s_list, txt2_input, foot_text, people_text)
print('\nНаибольшее кол-во людей, которые могут взять ролики: ', people_size(f_list, s_list))
