from keyboard import *
KEYBOARD = Keyboard("crescent", [[] for _ in range(10)])

def coord(i):
    row = 0
    col = i
    if i == 4:
        row = 1
        col -= 1
    if i == 5:
        row = 1
        col += 1
    key = KeyCoord(Pos(col, row, 0), col, row, Finger(i))
    return key

for col in range(10):
    key = coord(col)
    KEYBOARD.keymap[key.finger.value].append(key)

KEYBOARD.combos = []

for a in range(9):
    for b in range(a+1, 10):
        if 5 in {a, b}:
            continue
        KEYBOARD.combos.append(Combo([coord(a), coord(b)]))
