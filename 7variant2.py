def consolation(word, add='s'):
    global events
    a = []
    for i in range(len(events)):
        vord = events[i]
        if len(word) <= len(vord):
            vord = vord[:len(word)]
            a.append(str(vord).capitalize())
        else:
            while len(vord) != len(word):
                vord = vord + add
            a.append(str(vord).capitalize())
    events = tuple(i for i in a)
