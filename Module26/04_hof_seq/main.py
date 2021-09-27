from collections.abc import Iterable


def QHofstadter(lst: list, number=20) -> Iterable:
    lst1 = [1, 1]
    try:
        if lst == lst1:
            for i in range(2, number - 2):
                lst1.append(lst1[i - lst1[i - 1]] + lst1[i - lst1[i - 2]])
        else:
            raise StopIteration
    except StopIteration:
        print('Последовательность завершена!')
    return lst1


a = [1, 1]
b = [1, 2]
My_QHofstadter = QHofstadter(lst=a)
for item in My_QHofstadter:
    print(item, end=' ')
print('\n')
My_QHofstadter = QHofstadter(lst=b)
for item in My_QHofstadter:
    print(item, end=' ')
