import itertools

if __name__ == '__main__':
    i = 0
    all_code = itertools.product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], repeat=4)
    print('Все возможные коды:')
    for i_code in all_code:
        i += 1
        print(i_code)
    print(i)