## Import whichever keyboard and metric modules you want here.
from keyboards import matrix, matrix_thumbs, columnar, ansi, ansi_angle, combo_test, taipo, crescent, combo_16, chorded
from metrics import base, crescent_metrics, chorded_metrics

## The second field for each keyboard is the set of metric lists. You
## can have multiple per keyboard.
KEYBOARDS = [
    (matrix, [base]),
    (matrix_thumbs, [base]),
    (columnar, [base]),
    (ansi, [base]),
    (ansi_angle, [base]),
    (taipo, [chorded_metrics]),
    (crescent, [crescent_metrics]),
    (combo_16, [crescent_metrics]),
    (chorded, [chorded_metrics])
]


def flat_metric_list(arr):
    return [metric for mlist in arr for metric in mlist.METRIC_LIST]

KEYBOARDS = [(kb.KEYBOARD, flat_metric_list(mlist)) for (kb, mlist) in KEYBOARDS]
