import sys
a = list(map(str.strip, sys.stdin))
tbd = [0, 0]
for i in a:
    temp = list(map(str, i.split('; ')))
    c = 0
    ere = []
    for _ in temp:
        if len(str(_)) == 2:
            c += 1
            ere.append(_)
    if tbd[1] <= c:
        tbd = [ere, c]
for i in tbd[0]:
    print(i, end=' ')
