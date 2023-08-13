from keyboard import *
KEYBOARD = Keyboard("matrix", [])
for col in range(10):
    for row in range(3):
        if col == 4:
            finger = Finger.LI
        elif col == 5:
            finger = Finger.RI
        else:
            finger = Finger(col)
        key = KeyCoord(Pos(col, row, 0), col, row, finger)
        KEYBOARD.keys.append(key)
