from keyboard import *
KEYBOARD = Keyboard("matrix_thumbs", [[] for _ in range(10)])
for col in range(10):
    for row in range(3):
        if col == 4:
            finger = Finger.LI
        elif col == 5:
            finger = Finger.RI
        else:
            finger = Finger(col)
        key = KeyCoord(Pos(col, row, 0), col, row, finger)
        KEYBOARD.keymap[finger.value].append(key)

KEYBOARD.keymap[finger.LT.value].append(KeyCoord(Pos(4, 3, 0), 4, 3, Finger.LT))
KEYBOARD.keymap[finger.LT.value].append(KeyCoord(Pos(3, 3, 0), 3, 3, Finger.LT))
KEYBOARD.keymap[finger.RT.value].append(KeyCoord(Pos(5, 3, 0), 5, 3, Finger.RT))
KEYBOARD.keymap[finger.RT.value].append(KeyCoord(Pos(6, 3, 0), 6, 3, Finger.RT))
