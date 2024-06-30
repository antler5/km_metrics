from metrics.base import *

def is_repeat(a, b):
    return a == b

def is_sfb(a, b):
    return (not is_repeat(a, b)
            and has_same_finger(a, b))

METRIC_LIST = [
    Metric("Repeats", "rep", NgramType.BIGRAM, is_repeat, 1, False),
    Metric("Same-finger Bigrams", "sfb", NgramType.BIGRAM, is_sfb, 1, False),
    Metric("Same-finger Skipgrams", "sfs", NgramType.SKIPGRAM, is_sfb, 1, False),
    Metric("Alternation", "alt", NgramType.TRIGRAM, is_alternate, 1, False),
    Metric("Rolls", "roll", NgramType.TRIGRAM, is_roll, 1, False),
    Metric("Redirects", "redir", NgramType.TRIGRAM, is_redirect, 1, False),
    Metric("Trill Redirects", "trill-redir", NgramType.TRIGRAM, is_trill_redirect, 1, False),
]
