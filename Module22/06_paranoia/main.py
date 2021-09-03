def crypt(txt_line, n_shift):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a_list = [item for item in letters]
    return ''.join([(a_list[(n_shift + a_list.index(i_txt)) % len(a_list)]
                     if a_list.count(i_txt) == 1 else i_txt) for i_txt in txt_line])


def print_contents(file):
    with open(file, 'r', encoding='utf-8') as d_file:
        print('\nСодержимое файла:', file)
        for i_elem in d_file.readlines():
            print(i_elem, end='')
        print()


with open('cipher_text.txt', 'a', encoding='utf-8') as new_file:
    with open('text.txt', 'r', encoding='utf-8') as txt_file:
        print_contents(txt_file.name)
        ind = 0
        for i_line in txt_file.readlines():
            ind += 1
            new_file.write(str(crypt(i_line, ind)))
print_contents(new_file.name)
