def magic_word(a, backwards=True):
    global variants
    lupa = list(map(int, a.split()))
    lupa.sort(reverse=True)
    ts, st = lupa
    audi = []
    if backwards:
        for i in range(len(variants)):
            word = variants[i]
            newword = word[:st - 1]
            if (ts - st) % 2 == 0:
                for j in range((ts - st) // 2):
                    newword = newword + word[ts - j - 1]
                for j in range((ts - st) // 2):
                    newword = newword + word[st - j - 1]
            else:
                terpila = word[st + (ts - st) // 2 - 1]
                for j in range((ts - st) // 2 + 1):
                    newword = newword + word[ts - j - 1]
                newword = newword + terpila
                for j in range((ts - st) // 2 + 1):
                    if word[st + j - 1] != terpila:
                        newword = newword + word[st + j - 1]
            newword = newword + word[ts:]
            audi.append(newword)
    else:
        for i in range(len(variants)):
            word = variants[i]
            newword = word[:st - 1] + word[ts - 1] + word[st:ts - 1] + word[st - 1] + word[ts:]
            audi.append(newword)
    variants = tuple(i for i in audi)
