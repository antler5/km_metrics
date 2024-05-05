from keyboard import *
KEYBOARD = Keyboard("taipo", [[] for _ in range(10)])

def coord(col, row):
    fingers = [Finger.RI, Finger.RM, Finger.RR, Finger.RP]
    finger = fingers[col]
    key = KeyCoord(Pos(col, row, 0), col, row, finger)
    return key

for col in range(4):
    for row in range(2):
        key = coord(col, row)
        KEYBOARD.keymap[key.finger.value].append(key)

KEYBOARD.keymap[Finger.RT.value].append(KeyCoord(Pos(0, 2, 0), 0, 2, Finger.RT))

KEYBOARD.combos = [
    # thumb bichords
    Combo([coord(0,0), coord(0, 2)]),
    Combo([coord(1,0), coord(0, 2)]),
    Combo([coord(2,0), coord(0, 2)]),
    Combo([coord(3,0), coord(0, 2)]),
    Combo([coord(0,1), coord(0, 2)]),
    Combo([coord(1,1), coord(0, 2)]),
    Combo([coord(2,1), coord(0, 2)]),
    Combo([coord(3,1), coord(0, 2)]),

# top RI with rest
    Combo([coord(0,0), coord(1,0)]),
    Combo([coord(0,0), coord(2,0)]),
    Combo([coord(0,0), coord(3,0)]),
    Combo([coord(0,0), coord(1,1)]),
    Combo([coord(0,0), coord(2,1)]),
    Combo([coord(0,0), coord(3,1)]),

# bot RI with rest
    Combo([coord(0,1), coord(1,0)]),
    Combo([coord(0,1), coord(2,0)]),
    Combo([coord(0,1), coord(3,0)]),
    Combo([coord(0,1), coord(1,1)]),
    Combo([coord(0,1), coord(2,1)]),
    Combo([coord(0,1), coord(3,1)]),

# top RM with rest
    Combo([coord(1,0), coord(2,0)]),
    Combo([coord(1,0), coord(3,0)]),
    Combo([coord(1,0), coord(2,1)]),
    Combo([coord(1,0), coord(3,1)]),

# bot RM with rest
    Combo([coord(1,1), coord(2,0)]),
    Combo([coord(1,1), coord(3,0)]),
    Combo([coord(1,1), coord(2,1)]),
    Combo([coord(1,1), coord(3,1)]),

# top RR with rest
    Combo([coord(2,0), coord(3,0)]),
    Combo([coord(2,0), coord(3,1)]),

# bot RR with rest
    Combo([coord(2,1), coord(3,0)]),
    Combo([coord(2,1), coord(3,1)]),

# thumb trichords
# thumb + top RI with rest
    Combo([coord(0,0), coord(1,0), coord(0,2)]),
    Combo([coord(0,0), coord(2,0), coord(0,2)]),
    Combo([coord(0,0), coord(3,0), coord(0,2)]),
    Combo([coord(0,0), coord(1,1), coord(0,2)]),
    Combo([coord(0,0), coord(2,1), coord(0,2)]),
    Combo([coord(0,0), coord(3,1), coord(0,2)]),

# thumb + bot RI with rest
    Combo([coord(0,1), coord(1,0), coord(0,2)]),
    Combo([coord(0,1), coord(2,0), coord(0,2)]),
    Combo([coord(0,1), coord(3,0), coord(0,2)]),
    Combo([coord(0,1), coord(1,1), coord(0,2)]),
    Combo([coord(0,1), coord(2,1), coord(0,2)]),
    Combo([coord(0,1), coord(3,1), coord(0,2)]),

# thumb + top RM with rest
    Combo([coord(1,0), coord(2,0), coord(0,2)]),
    Combo([coord(1,0), coord(3,0), coord(0,2)]),
    Combo([coord(1,0), coord(2,1), coord(0,2)]),
    Combo([coord(1,0), coord(3,1), coord(0,2)]),

# thumb + bot RM with rest
    Combo([coord(1,1), coord(2,0), coord(0,2)]),
    Combo([coord(1,1), coord(3,0), coord(0,2)]),
    Combo([coord(1,1), coord(2,1), coord(0,2)]),
    Combo([coord(1,1), coord(3,1), coord(0,2)]),

# thumb + top RR with rest
    Combo([coord(2,0), coord(3,0), coord(0,2)]),
    Combo([coord(2,0), coord(3,1), coord(0,2)]),

# thumb + bot RR with rest
    Combo([coord(2,1), coord(3,0), coord(0,2)]),
    Combo([coord(2,1), coord(3,1), coord(0,2)]),
]
