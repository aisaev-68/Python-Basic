import collections


def bar_graph(str_txt):
    for sym in str_txt:
        count = 0
        for item in str_txt:
            if sym == item:
                count += 1
        dict_bargraph[sym] = count


def invert_dict():
    print('\nИнвертированный словарь частот:')
    d = collections.defaultdict(list)
    for key, value in dict_bargraph.items():
        d[value].append(key)
    for k, v in d.items():
        print(f'{k} : {v}')


dict_bargraph = dict()
txt = input('Введите текст: ')
bar_graph(txt)
print('Оригинальный словарь частот:')
for key1, value1 in sorted(dict_bargraph.items()):
    print(key1, ' : ', value1)
invert_dict()
