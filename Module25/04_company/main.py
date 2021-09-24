class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        if isinstance(self, Manager):
            self.var = 'Менеджер'
        elif isinstance(self, Agent):
            self.var = 'Агент'
        elif isinstance(self, Worker):
            self.var = 'Рабочий'
        wages = self.payroll_method()
        return '{} {} {}, возраст {} лет, получает зарплату в размере {}'.format(self.var, self.__surname, self.__name,
                                                                                 self.__age, wages)


class Employee(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def payroll_method(self):
        return 0


class Manager(Employee):
    __wages = 13000

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def payroll_method(self):
        return self.__wages


class Agent(Employee):
    __salary = 5000

    def __init__(self, name, surname, age, volume_sales):
        super().__init__(name, surname, age)
        self.__volume_sales = volume_sales

    def payroll_method(self):
        return round(self.__salary + self.__volume_sales / 20, 2)


class Worker(Employee):
    def __init__(self, name, surname, age, hours_worked):
        super().__init__(name, surname, age)
        self.__hours_worked = hours_worked

    def payroll_method(self):
        return 100 * self.__hours_worked


manag1 = Manager('Сергей', 'Иванов', 28)
manag2 = Manager('Петр', 'Шувалов', 30)
manag3 = Manager('Иван', 'Шварц', 43)
print('{}\n{}\n{}'.format(manag1, manag2, manag3))
agent1 = Agent('Борис', 'Петров', 33, 200000)
agent2 = Agent('Александр', 'Кравчук', 20, 240000)
agent3 = Agent('Харитон', 'Богданов', 46, 300000)
print('\n{}\n{}\n{}'.format(agent1, agent2, agent3))
worker1 = Worker('Виктор', 'Морозов', 45, 165)
worker2 = Worker('Евгений', 'Крылов', 50, 178)
worker3 = Worker('Виктория', 'Нуланд', 55, 140)
print('\n{}\n{}\n{}'.format(worker1, worker2, worker3))
