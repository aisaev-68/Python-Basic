def f_comb(logic,basic_list, side_list, n):
    basic_list.extend(side_list)
    numb_count = basic_list.count(n)
    if logic:
        for i in basic_list:
            if int(i) == n:
                basic_list.remove(i)
    return numb_count


a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
print('Кол-во цифр 5 при первом объединении:', f_comb(True, a, b, 5),
      '\nКол-во цифр 3 при втором объединении:', f_comb(False, a, c, 3),
      '\nИтоговый список:', a)