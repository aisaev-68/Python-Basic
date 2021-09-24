class MyDict(dict):
    def __init__(self, my_dict):
        super().__init__()
        self.__my_dict = my_dict

    def get(self, key):
        if self.__my_dict.get(key) == None:
            return 0
        else:
            return self.__my_dict.get(key)


new_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
md = MyDict(new_dict)
print('Когда ключ не содержиться в словаре метод возвращает {}'.format(md.get(0)))
print('Когда ключ содержиться в словаре метод возвращает {}'.format(md.get(3)))
