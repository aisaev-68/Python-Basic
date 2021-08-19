def ip_check(ip_adr):
    count = len(ip_adr)
    for i in range(len(ip_adr)):
        if ip_adr[i].isdigit():
            if int(ip_adr[i]) > 255:
                print(f'{ip_adr[i]} превышает 255')
                count -= 1
        else:
            print(f'{ip_adr[i]} - не целое число')
            count -= 1
    if count == len(ip_adr):
        return True
    else:
        return False


def str_check(ip_txt):
    count = 0
    for item in ip_txt:
        if item == '.':
            count += 1
    if count == 3:
        return True
    else:
        return False


ip_ad = input('Введите IP: ')
if str_check(ip_ad):
    if ip_check(ip_ad.split('.')):
        print('IP-адрес корректен')
else:
    print('Адрес - это четыре числа, разделённые точками')
