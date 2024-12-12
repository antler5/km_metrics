from metrics.base import *

def thumb_combo(a, b):
    return (isinstance(a, Combo)
            and True in split(lambda a, b: a.finger == Finger.RT, a, b))

def pinkie(a, b):
    return True in split(lambda a, b: a.finger == Finger.RP, a, b)

def pinkie_top(a, b):
    return True in split(lambda a, b: a.finger == Finger.RP and a.pos.row == 0, a, b)

def pinkie_combo_x_rows(a, b):
    tmp_val=None
    def tmp(x):
      nonlocal tmp_val
      tmp_val = x
      return True
    return (isinstance(a, Combo) # for clarity
            and True in split(lambda a, b: a.finger == Finger.RP and tmp(a.pos.row), a, b)
            and True in split(lambda a,b: a.pos.row is not tmp_val, a, b))

def pinkie_seq_x_rows(a, b):
    tmp_val=None
    def tmp(x):
      nonlocal tmp_val
      tmp_val = x
      return True
    return (True in split(lambda a, b: b.finger == Finger.RP and tmp(b.pos.row), a, b)
            # Thumb is OK
            and True in split(lambda a, b: a.pos.row not in (tmp_val, 2), a, b))

# This is manipulated by the evaluator to apply layout-wide metrics.
def dummy_metric(_a, _b):
    return False

METRIC_LIST = [
    # Upstream
    Metric("Same-finger Repeats", "sfr", NgramType.BIGRAM, is_sfr, 1, True),
    Metric("Same-finger Bigrams", "sfb", NgramType.BIGRAM, is_sfb, 1, True),
    Metric("Same-finger Skipgrams", "sfs", NgramType.SKIPGRAM, is_sfb, 1, True),
    Metric("Same-finger Bigram Distance", "sfb-dist", NgramType.BIGRAM, is_sfb, distance, True),
    Metric("Same-finger Skipgram Distance", "sfs-dist", NgramType.SKIPGRAM, is_sfb, distance, True),
    Metric("Redirects", "redir", NgramType.TRIGRAM, is_redirect, 1, False),
    Metric("Trill Redirects", "trill-redir", NgramType.TRIGRAM, is_trill_redirect, 1, False),
    Metric("Mini 3rolls", "m3roll", NgramType.TRIGRAM, is_mini3roll, 1, False),
    Metric("Misc Tristrokes", "misc", NgramType.TRIGRAM, misc_trigram, 1, False),
    Metric("Same-finger-skip Redirects", "sfs-redir", NgramType.TRIGRAM, is_sfs_redirect, 1, False),

    # Bespoke
    Metric("Thumb Combos", "thumb", NgramType.BIGRAM, thumb_combo, 1, False),
    Metric("Pinkie Use", "pinkie", NgramType.BIGRAM, pinkie, 1, False),
    Metric("Top Pinkie Combos", "top-pinkie", NgramType.BIGRAM, pinkie_top, 1, False),
    Metric("Pinkie Across Rows", "pinkie-x", NgramType.BIGRAM, pinkie_combo_x_rows, 1, False),
    Metric("Pinkie Seq Across Rows", "pinkie-seq-x", NgramType.BIGRAM, pinkie_seq_x_rows, 1, False),

    # Meta
    Metric("Dummy Metric", "dummy", NgramType.BIGRAM, dummy_metric, 1, False),
]
