from keyboard import *
KEYBOARD = Keyboard("16key", [[] for _ in range(10)])

def coord(col, row, finger):
    key = KeyCoord(Pos(col, row, 0), col, row, finger)
    return key

coords = []
for i in range(10):
    col = i
    row = 1
    if i == 4:
        row += 1
        col -= 1
    elif i == 5:
        row += 1
        col += 1
    coords.append(coord(col, row, Finger(i)))
    if 1 <= i <= 3 or 6 <= i <= 8:
        coords.append(coord(col, 0, Finger(i)))

for key in coords:
    KEYBOARD.keymap[key.finger.value].append(key)

KEYBOARD.combos = []

for i, a in enumerate(coords):
    for j, b in enumerate(coords[i+1:]):
        if 4 in {i, j} or a.finger == b.finger:
            continue
        KEYBOARD.combos.append(Combo([a, b]))
