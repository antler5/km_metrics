from math import sqrt
from enum import Enum
from metric import *

Direction = Enum("Direction", ["INWARD", "OUTWARD", "NONE"])

def direction(a, b):
    if a.finger == b.finger or a.finger.hand() != b.finger.hand():
        return Direction.NONE
    if a.finger.kind().value < b.finger.kind().value:
        return Direction.INWARD
    return Direction.OUTWARD

def x_distance(a, b):
    return abs(a.x - b.x)

def y_distance(a, b):
    return abs(a.y - b.y)

def distance(a, b):
    return sqrt(x_distance(a, b) ** 2 +
         y_distance(a, b) ** 2)

def is_sfr(a, b):
    return a == b

def is_sfb(a, b):
    return (not is_sfr(a, b)
            and a.finger == b.finger)

def is_lsb(a, b):
    return (a.finger.hand() == b.finger.hand()
            and abs(a.finger.kind().value - b.finger.kind().value) == 1
            and x_distance(a, b) >= 2)

def is_alternate(a, b, c):
    return (a.finger.hand() != b.finger.hand()
            and a.finger.hand() == c.finger.hand())

def is_roll(a, b, c):
    return (a.finger.hand() != c.finger.hand()
            and b.finger != a.finger
            and b.finger != c.finger)

def is_redirect(a, b, c):
    return (a.finger.hand() == b.finger.hand() == c.finger.hand()
            and a.finger != b.finger
            and b.finger != c.finger
            and direction(a, b) != direction(b, c))

def is_same_row_roll(a, b, c):
    return (is_roll(a, b, c)
            and a.pos.row == b.pos.row == c.pos.row)

METRIC_LIST = [
    Metric("Same-finger Repeats", "sfr", NgramType.BIGRAM, is_sfr, 1),
    Metric("Same-finger Bigrams", "sfb", NgramType.BIGRAM, is_sfb, 1),
    Metric("Same-finger Skipgrams", "sfs", NgramType.SKIPGRAM, is_sfb, 1),
    Metric("Same-finger Bigram Distance", "sfb-dist", NgramType.BIGRAM, is_sfb, distance),
    Metric("Same-finger Skipgram Distance", "sfs-dist", NgramType.SKIPGRAM, is_sfb, distance),
    Metric("Lateral Stretch Bigrams", "lsb", NgramType.BIGRAM, is_lsb, 1),
    Metric("Lateral Stretch Bigram Distance", "lsb-dist", NgramType.BIGRAM, is_lsb, x_distance),
    Metric("Alternates", "alt", NgramType.TRIGRAM, is_alternate, 1),
    Metric("Rolls", "roll", NgramType.TRIGRAM, is_roll, 1),
    Metric("Same-row Rolls", "sr-roll", NgramType.TRIGRAM, is_same_row_roll, 1),
    Metric("Redirects", "redir", NgramType.TRIGRAM, is_redirect, 1)
]
