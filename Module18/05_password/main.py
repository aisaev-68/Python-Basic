def check_password():
    txt = input('Придумайте пароль: ')
    up_elem_count = 0
    digit_count = 0
    for item in txt:
        if item.isalpha() and item.lower() != item:
            up_elem_count += 1
        elif item.isdigit():
            digit_count += 1
    if up_elem_count >= 1 and digit_count >= 3 and len(txt) >= 8:
        print('\nЭто надёжный пароль!')
    else:
        print('\nПароль ненадёжный. Попробуйте ещё раз.\n')
        check_password()


check_password()
