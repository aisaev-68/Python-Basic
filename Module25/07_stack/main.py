class Stack:
    def __init__(self):
        self.stack = {}

    def add_steck(self, tsk1, tsk2):
        if not self.stack.get(tsk2):
            self.stack[tsk2] = [tsk1]

        else:
            self.stack[tsk2].append(tsk1)

    def del_steck(self, tsk1, tsk2):
        if self.stack.get(tsk2):
            self.stack.pop(tsk2)
        else:
            print('В стеке отсутствует элемент {}'.format(tsk1))

    def getdict(self):
        return self.stack


class TaskManager:
    def __init__(self):
        self.stak = Stack()

    def new_task(self, tsk1, tsk2):
        self.stak.add_steck(tsk1, tsk2)

    def del_task(self, tsk1, tsk2):
        self.stak.del_steck(tsk1, tsk2)

    def __str__(self):
        my_dict = sorted(self.stak.getdict().keys())
        txt = 'Результат:\n\n'
        for key in my_dict:
            words = ', '.join(self.stak.getdict()[key])
            txt += f'{key} {words}\n'
        return txt


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
manager.del_task("помыть посуду", 4)
print(manager)
