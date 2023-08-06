from metric import *

def distance(a, b):
    sqrt((a.x - b.x) ** 2 +
         (a.y - b.y) ** 2)

def is_sfr(a, b):
    return a == b

METRIC_LIST = [
    Metric("Same-finger Repeat", "sfr", NgramType.BIGRAM, is_sfr, 1),
    Metric("Same-finger Repeat Distance", "sfr-dist", NgramType.BIGRAM, is_sfr, distance)
]
