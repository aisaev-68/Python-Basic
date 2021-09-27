from typing import Any


class LinkedList:
    class Node:
        def __init__(self, data=None, link=None):
            self.data = data
            self.link = link

    def __init__(self):
        self.head = None

    def append(self, val: Any) -> None:
        new_node = self.Node(val)
        if self.head == None:
            self.head = new_node
        else:
            prev_node = self.head
            while prev_node.link != None:
                prev_node = prev_node.link
            prev_node.link = new_node

    def get(self, index: int) -> Any:
        counter = 0
        node = self.head
        if index == 0:
            node = node.data
            return node
        try:
            while index != counter or node.link != None:
                node = node.link
                counter += 1
                if index == counter:
                    node = node.data
                    break
            else:
                raise AttributeError
        except AttributeError:
            return f'\nОшибка! Индекс списка вне допустимого диапазона'
        else:
            return node

    def remove(self, index: int) -> None:
        counter = 0
        try:
            if index == 0:
                self.head = self.head.link
                return
            node = self.head
            prev_node = node
            while counter < index:
                prev_node = node
                node = node.link
                counter += 1
            prev_node.link = node.link
            del node
        except AttributeError:
            print('Ошибка! Индекс списка вне допустимого диапазона')

    def __str__(self) -> str:
        txt = ''
        node = self.head
        while node != None:
            txt += f'{node.data} '
            node = node.link
        return f'[{txt.strip()}]'


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
my_list.append(60)
my_list.append('A')
print('Результат:')
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
