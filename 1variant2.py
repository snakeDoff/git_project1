def parchment(a, divisor=' '):
    global snuffbox
    gab = []
    a = set(a)
    for i in range(len(snuffbox)):
        word = set(snuffbox[i])
        tt = word - a
        gab.append(divisor.join(list(tt)))
    snuffbox = tuple(i for i in gab)
