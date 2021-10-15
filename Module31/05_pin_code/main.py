import itertools

if __name__ == '__main__':
    all_code = itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], r=4)
    print('Все возможные коды:')
    for i_code in all_code:
        print(i_code)
