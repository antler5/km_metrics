from keyboard import *
KEYBOARD = Keyboard("ansi", [])
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
        key = KeyCoord(Pos(col, row, 0), stagger+col, row, finger)
        KEYBOARD.keys.append(key)
