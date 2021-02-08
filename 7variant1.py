import sys
a = list(map(str.strip, sys.stdin))
tbd = [0, 0]
for i in a:
    temp = list(map(str, i.split(' ')))
    c = 0
    ere = []
    for _ in temp:
        if len(_) != 2:
            c += 1
            ere.append(str(_))
    if tbd[1] < c:
        tbd = [ere, c]
print('*'.join(tbd[0]))
