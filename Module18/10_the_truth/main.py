txt_crypt = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj ' \
            'scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib ' \
            'oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo ' \
            'djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst ' \
            'tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj ' \
            'gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof ' \
            'pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv' \
            '( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op ' \
            'gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt ' \
            'fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. ' \
            'fu(tm pe psfn gp tf"uip'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def encrypt(crypt, shift):
    txt_encrypt = ''
    word_encrypt = []
    for item in crypt:
        if item in alphabet:
            index = alphabet.index(item)
            txt_encrypt += alphabet[(index - shift) % len(alphabet)]
        else:
            if item == '/':
                txt_encrypt += '.'
            elif item == '-':
                txt_encrypt += ','
            elif item == '(':
                txt_encrypt += '`'
            elif item == '.':
                txt_encrypt += '-'
            elif item == '"':
                txt_encrypt += '!'
            elif item == '+':
                txt_encrypt += ''
            else:
                txt_encrypt += item
    txt = txt_encrypt.split()
    print(txt_encrypt)
    index_elem = -3
    for elem in txt:
        ind = (index_elem + len(elem)) % len(elem)
        word_encrypt.append(elem[ind:] + elem[:ind])
        for i_symb in elem:
            if i_symb == '.':
                index_elem -= 1
                break
    return ' '.join(word_encrypt)


s = ''
lst = encrypt(txt_crypt, 1)
print('\nРасшифрованный текст:\n', end=' ')
for item in lst:
    s += item
    if item == '.':
        print(s, end='')
        print()
        s = ''
