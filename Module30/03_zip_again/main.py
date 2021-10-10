from typing import List

strings: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

if __name__ == '__main__':
    print('Результат работы программы:')
    results: List[tuple] = [(x, y) for ind_x, x in enumerate(strings) for ind_y, y in enumerate(numbers) if ind_y == ind_x]
    print(results)
