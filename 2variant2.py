def animal_language(n, show=0):
    global chatter
    ff = []
    for i in range(len(chatter)):
        if show == 0:
            ff.append(str(chatter[i][n::n]))
        if show == 1:
            ff.append(str(chatter[i][n::n]).lower())
        if show == 2:
            ff.append(str(chatter[i][n::n]).upper())
        if show == 3:
            ff.append(str(chatter[i][n::n]).capitalize())
    chatter = tuple(i for i in ff)
