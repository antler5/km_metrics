from keyboard import *
KEYBOARD = Keyboard("2x4_some_chords", [[] for _ in range(10)])

def coord(col, row):
    fingers = [Finger.RI, Finger.RM, Finger.RR, Finger.RP]
    finger = fingers[col]
    key = KeyCoord(Pos(col, row, 0), col, row, finger)
    return key

for col in range(4):
    for row in range(2):
        key = coord(col, row)
        KEYBOARD.keymap[key.finger.value].append(key)

coords = [(col,row)
          for col in range(0,4)
          for row in range(0,2)]

# bichords
combos = set([
    frozenset((a,b))
    for a in coords
    for b in coords
    if len(set([a,b])) == 2
    # Same-row combos only.
    and len(set(map(lambda x: x[1], [a,b]))) == 1
])

# trichords
combos = combos.union(set([
    frozenset((a,b,c))
    for a in coords
    for b in coords
    for c in coords
    if len(set([a,b,c])) == 3
    # Stacks on the same finger are ok, but not with a third key.
    and len(set(map(lambda x: x[0], [a,b,c]))) == 3
    # Same-row combos only.
    and len(set(map(lambda x: x[1], [a,b,c]))) == 1
]))

# Whitelist of cross-row combos

# BRP & Top row singles
combos = combos.union(set([
    frozenset(((3,1),b))
    for b in [(col,0) for col in [0,1,2]]
]))

# BRP & Top row doubles
combos = combos.union(set([
    frozenset(((3,1),b,c))
    for b in [(col,0) for col in [0,1,2]]
    for c in [(col,0) for col in [0,1,2]]
    if b != c
]))

# BRR & TRI
combos = combos.union(set([frozenset(((2,1),(0,0)))]))

KEYBOARD.combos = [Combo(list(map(lambda col,row: coord(col,row), *zip(*xs))))
                   for xs in sorted(combos)]
