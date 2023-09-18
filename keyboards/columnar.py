from keyboard import *
KEYBOARD = Keyboard("columnar", [[] for _ in range(10)])
stagger = [0, 0.2, 0.25, 0.15, 0.10, 0.10, 0.15, 0.25, 0.2, 0]
for col in range(10):
    for row in range(3):
        if col == 4:
            finger = Finger.LI
        elif col == 5:
            finger = Finger.RI
        else:
            finger = Finger(col)
        key = KeyCoord(Pos(col, row, 0), col, row - stagger[col], finger)
        KEYBOARD.keymap[finger.value].append(key)
