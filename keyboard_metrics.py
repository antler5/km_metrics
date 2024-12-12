## Import whichever keyboard and metric modules you want here.
from keyboards import ansi, ansi_angle, 2x4_all_chords, 2x4_some_chords, 2x4_2t_all_chords, 2x4_2t_some_chords, columnar, columnar_thumbs, combo_16, combo_test, crescent, matrix, matrix_thumbs, taipo
from metrics import base, crescent_metrics, 2x4_2t_some_chords_metrics

## The second field for each keyboard is the set of metric lists. You
## can have multiple per keyboard.
KEYBOARDS = [
    # (matrix, [base]),
    # (matrix_thumbs, [base]),
    (columnar, [base]),
    (columnar_thumbs, [base]),
    # (ansi, [base]),
    # (ansi_angle, [base]),
    # (taipo, [2x4_2t_some_chords_metrics]),
    # (crescent, [crescent_metrics]),
    # (combo_16, [crescent_metrics]),
    (2x4_all_chords, [2x4_all_chords_metrics]),
    (2x4_some_chords, [2x4_some_chords_metrics]),
    (2x4_2t_all_chords, [2x4_2t_all_chords_metrics]),
    (2x4_2t_some_chords, [2x4_2t_some_chords_metrics])
]


def flat_metric_list(arr):
    return [metric for mlist in arr for metric in mlist.METRIC_LIST]

KEYBOARDS = [(kb.KEYBOARD, flat_metric_list(mlist)) for (kb, mlist) in KEYBOARDS]
