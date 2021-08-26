def is_prime(list_tup_let_lis_dic, list_prime):
    numb = 0
    for item in list_tup_let_lis_dic:
        count = 0
        for elem in item:
            if count >= 2:
                for i in range(2, count + 1):
                    if count % i == 0:
                        numb = i
                        break
                if count == numb:
                    list_prime.append(elem)
            count += 1
    return list_prime


def prime(list_prime, lst2):
    return is_prime(list_prime, lst2)


lst1 = []
lst = [] # внутри списка должны быть (кортеж, строка, список, словарь)
my_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' # строка
my_tuple = tuple(i for i in my_letter) # кортеж
lst.append(my_tuple)
lst.append(my_letter)
my_list = list(my_tuple) #список
lst.append(my_list)
my_dict = {key: my_letter[key] for key in range(len(my_letter))} # словарь
lst.append(my_dict)
print(prime(lst, lst1))
