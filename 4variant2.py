def magic_word(st, backwards=True):
    global variants
    sp = [i for i in variants]
    ff = []
    a, b = list(map(int, st.split(' ')))
    for i in sp:
        word = ''
        if not backwards:
            word = i[:a - 1] + i[b - 1] + i[a:b - 1] + i[a - 1] + i[b:]
            ff.append(word)
    print(ff)


variants = ('murtubor', 'murbutor', 'murburbur')
magic_word('4 6', backwards=False)
