from keyboard import *
KEYBOARD = Keyboard("ansi-angle", [[] for _ in range(10)])
for col in range(10):
    for row in range(3):
        stagger = 0
        if row == 1:
            stagger = 0.25
        elif row == 2:
            stagger = 0.75
        if col == 4:
            finger = Finger.LI
        elif col == 5:
            finger = Finger.RI
        else:
            finger = Finger(col)
        if row == 2 and col <= 4 and col >= 1:
            stagger -= 1
        if row == 2 and col == 0:
            break
        key = KeyCoord(Pos(col, row, 0), stagger+col, row, finger)
        KEYBOARD.keymap[finger.value].append(key)

key = KeyCoord(Pos(4, 2, 0), 4.75, 2, Finger.LI)
KEYBOARD.keymap[Finger.LI.value].append(key)
