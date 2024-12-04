from metrics.base import *

METRIC_LIST = [
    Metric("Same-finger Repeats", "sfr", NgramType.BIGRAM, is_sfr, 1, True),
    Metric("Same-finger Bigrams", "sfb", NgramType.BIGRAM, is_sfb, 1, True),
    Metric("Same-finger Skipgrams", "sfs", NgramType.SKIPGRAM, is_sfb, 1, True),
    Metric("Same-finger Bigram Distance", "sfb-dist", NgramType.BIGRAM, is_sfb, distance, True),
    Metric("Same-finger Skipgram Distance", "sfs-dist", NgramType.SKIPGRAM, is_sfb, distance, True),
    Metric("Redirects", "redir", NgramType.TRIGRAM, is_redirect, 1, False),
    Metric("Same-finger-skip Redirects", "sfs-redir", NgramType.TRIGRAM, is_sfs_redirect, 1, False),
    Metric("Trill Redirects", "trill-redir", NgramType.TRIGRAM, is_trill_redirect, 1, False),
]
