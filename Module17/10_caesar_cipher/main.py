a_list = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р",
          "с", "т", "у", "ф", "х", "ц", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
first_word = input("Введите сообщение: ")
n_shift = int(input("Введите сдвиг: "))
print("\nЗашифрованное сообщение: ", ''.join([(a_list[(n_shift + a_list.index(i_txt)) % len(a_list)]
                                               if a_list.count(i_txt) == 1 else i_txt) for i_txt in
                                              first_word]))
