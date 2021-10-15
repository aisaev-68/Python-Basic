import re

znak: str = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

if __name__ == '__main__':
    print('Результат:')
    result = re.findall(r'\b\w\d{3}\w{2}\d{2,3}\b', znak)
    print('Список номеров частных автомобилей:', result)

    result = re.findall(r'\b\w{2}\d{3}\d{2,3}\b', znak)
    print('Список номеров такси:', result)
