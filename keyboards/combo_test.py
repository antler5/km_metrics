from keyboard import *
KEYBOARD = Keyboard("combo_test", [[] for _ in range(10)])

def coord(col, row):
    fingers = [Finger.LP, Finger.LR, Finger.LM, Finger.LI, Finger.LI,
               Finger.RI, Finger.RI, Finger.RM, Finger.RR, Finger.RP]
    finger = fingers[col]
    key = KeyCoord(Pos(col, row, 0), col, row, finger)
    return key

for col in range(10):
    for row in range(3):
        key = coord(col, row)
        KEYBOARD.keymap[key.finger.value].append(key)

KEYBOARD.combos = [
    Combo([coord(1,1), coord(2,1)]),
    Combo([coord(7,1), coord(8,1)])
]
