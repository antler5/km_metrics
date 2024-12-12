from keyboard import *
KEYBOARD = Keyboard("2x4_2t_all_chords", [[] for _ in range(10)])

def coord(col, row):
    fingers = [Finger.RI, Finger.RM, Finger.RR, Finger.RP]
    finger = Finger.RT if row == 2 else fingers[col]
    key = KeyCoord(Pos(col, row, 0), col, row, finger)
    return key

for col in range(4):
    for row in range(2):
        key = coord(col, row)
        KEYBOARD.keymap[key.finger.value].append(key)

KEYBOARD.keymap[Finger.RT.value].append(KeyCoord(Pos(0, 2, 0), 0, 2, Finger.RT))
KEYBOARD.keymap[Finger.RT.value].append(KeyCoord(Pos(1, 2, 0), 1, 2, Finger.RT))

coords = [(col,row)
          for col in range(0,4)
          for row in range(0,2)]
coords.append((0,2))
coords.append((1,2))

# bichords
combos = set([
    frozenset((a,b))
    for a in coords
    for b in coords
    if len(set([a,b])) == 2
])

# trichords
combos = combos.union(set([
    frozenset((a,b,c))
    for a in coords
    for b in coords
    for c in coords
    if len(set([a,b,c])) == 3
]))

# thumb bichords
combos = combos.union(set([
    frozenset((a,b))
    for a in [(0,2),(1,2)]
    for b in coords
    if len(set([a,b])) == 2
]))

# thumb trichords
combos = combos.union(set([
    frozenset((a,b,c))
    for a in [(0,2),(1,2)]
    for b in coords
    for c in coords
    if len(set([(0,2),b,c])) == 3
]))

KEYBOARD.combos = [Combo(list(map(lambda col,row: coord(col,row), *zip(*xs))))
                   for xs in sorted(combos)]

# Add z/space 4-chords to model artsey more accurately.
KEYBOARD.combos += [
    Combo([coord(0,0),coord(1,0),coord(2,0),coord(3,0)]),
    Combo([coord(0,1),coord(1,1),coord(2,1),coord(3,1)])
]

