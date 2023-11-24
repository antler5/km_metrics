from keyboard import *
KEYBOARD = Keyboard("ansi", [[] for _ in range(10)])
staggers = [0, 0.25, 0.75]
for col in range(10):
    for row in range(3):
        stagger = staggers[row]
        if col == 4:
            finger = Finger.LI
        elif col == 5:
            finger = Finger.RI
        else:
            finger = Finger(col)
        key = KeyCoord(Pos(col, row, 0), stagger+col, row, finger)
        KEYBOARD.keymap[finger.value].append(key)
