from math import sqrt
from metric import *

def distance(a, b):
    return sqrt((a.x - b.x) ** 2 +
         (a.y - b.y) ** 2)

def is_sfr(a, b):
    return a == b

def is_sfb(a, b):
    return (not is_sfr(a, b)
            and a.finger == b.finger)

METRIC_LIST = [
    Metric("Same-finger Repeat", "sfr", NgramType.BIGRAM, is_sfr, 1),
    Metric("Same-finger Bigram", "sfb", NgramType.BIGRAM, is_sfb, 1),
    Metric("Same-finger Skipgram", "sfs", NgramType.SKIPGRAM, is_sfb, 1),
    Metric("Same-finger Bigram Distance", "sfb-dist", NgramType.BIGRAM, is_sfb, distance),
    Metric("Same-finger Skipgram Distance", "sfs-dist", NgramType.SKIPGRAM, is_sfb, distance)
]
