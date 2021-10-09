class File:
    def __init__(self, filename) -> None:
        self.__filename = filename

    def __enter__(self) -> 'file':
        try:
            self.open_file = open(self.__filename, 'r', encoding='utf-8')
            print('Файл существует в текущем каталоге и открыть в режиме чтения.')
        except Exception:
            self.open_file = open(self.__filename, 'w', encoding='utf-8')
            print('Создан новый файл и открыть в режиме записи.')
        return self.open_file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.open_file.close()
        return True


file = File('readme.txt')
with file as new_file:
    pass
