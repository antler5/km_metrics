from keyboard import *
KEYBOARD = Keyboard("chorded", [[] for _ in range(10)])

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

coords = [(col,row)
          for col in range(0,4)
          for row in range(0,2)]
coords.append((0,2))

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
    # Stacks on the same finger are ok, but not with a third key.
    and len(set(map(lambda x: x[0], [a,b,c]))) == 3
]))

KEYBOARD.combos = [Combo(list(map(lambda col,row: coord(col,row), *zip(*xs))))
                   for xs in sorted(combos)]

# Add z/space 4-chords to model artsey more accurately.
KEYBOARD.combos += [
    Combo([coord(0,0),coord(1,0),coord(2,0),coord(3,0)]),
    Combo([coord(0,1),coord(1,1),coord(2,1),coord(3,1)])
]

def finger(c):
    match c:
        case (0,0):
            return "TRI"
        case (1,0):
            return "TRM"
        case (2,0):
            return "TRR"
        case (3,0):
            return "TRP"
        case (0,1):
            return "BRI"
        case (1,1):
            return "BRM"
        case (2,1):
            return "BRR"
        case (3,1):
            return "BRP"
        case (0,2):
            return "RT"
        case _:
            print("fuck")
            quit()

for x in KEYBOARD.combos:
    print([finger((y.x,y.y)) for y in x.coords])
