## Import whichever keyboard and metric modules you want here.
from keyboards import matrix, columnar, ansi, ansi_angle, combo_test
from metrics import base

## The second field for each keyboard is the set of metric lists. You
## can have multiple per keyboard.
KEYBOARDS = [
    (matrix, [base]),
    (columnar, [base]),
    (ansi, [base]),
    (ansi_angle, [base]),
    (combo_test, [base])
]


def flat_metric_list(arr):
    return [metric for mlist in arr for metric in mlist.METRIC_LIST]

KEYBOARDS = [(kb.KEYBOARD, flat_metric_list(mlist)) for (kb, mlist) in KEYBOARDS]
