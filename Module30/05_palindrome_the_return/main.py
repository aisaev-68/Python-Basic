import collections


def can_be_poly(txt: str) -> bool:
    letter_dict = collections.Counter(list(txt))
    letter = ''
    for item in letter_dict:
        if letter and letter_dict[item] % 2 == 1:
            return False
        elif letter_dict[item] % 2 == 1:
            letter = item
    return True


if __name__ == '__main__':
    print(can_be_poly('ababc'))

    print(can_be_poly('abbbc'))
