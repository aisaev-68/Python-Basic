class Date:
    def __init__(self, day: int = 0, month: int = 0, year: int = 0):
        self.__day = day
        self.__month = month
        self.__year = year

    @classmethod
    def from_string(cls, val_date: str) -> 'Date':
        if cls.is_date_valid(val_date):
            day, month, year = val_date.split('-')
            return cls(day, month, year)


    @classmethod
    def is_date_valid(cls, value: str) -> bool:
        count = 0
        try:
            day, month, year = value.split('-')
            leap_year = 366 if ((int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0)) else 365
            if leap_year == 366 and int(month) == 2:
                if 1 <= int(day) <= 29:
                    count += 1
            else:
                if 1 <= int(day) <= 28 and int(month) == 2:
                    count += 1
            if 1 <= int(day) <= 31 and int(month) != 2:
                count += 1
            if 1 <= int(month) <= 12:
                count += 1
            if int(year) >= 1800:
                count += 1
            return True if count == 3 else False
        except ValueError:
            return False

    def __str__(self) -> str:
        return f'День: {self.__day} Месяц: {self.__month} Год: {self.__year}'

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('29-02-2013'))
print(Date.is_date_valid('31-12-2077'))
