import timeit

if __name__ == '__main__':
    res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print('Результат: ', res)
    res_list: float = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
    print('Результат с использованием list comprehensions: ', res_list)
    res_map: float = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
    print('Результат с использованием map: ', res_map)
