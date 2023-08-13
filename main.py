import json
import itertools
from enum import Enum
from typing import List
from metrics import base
from keyboard import *
from metric import *

class KeymeowEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Pos):
            return {"row": o.row, "col": o.col, "layer": o.layer}
        if isinstance(o, Finger):
            return o.name
        if isinstance(o, KeyCoord):
            return {"pos": o.pos, "x": o.x, "y": o.y, "finger": o.finger.name}
        if isinstance(o, Keyboard):
            return {"keys": o.keys}

        return super().default(o)

NstrokeType = Enum("NstrokeType", ["MONOSTROKE", "BISTROKE", "TRISTROKE"])

class Nstroke:
    def __init__(self, kind: NstrokeType, nstroke: List[int]):
        self.kind = kind
        self.nstroke = nstroke

class MetricAmount:
    def __init__(self, metric: int, amount: float):
        self.metric = metric
        self.amount = amount

class NstrokeData:
    def __init__(self, nstroke: Nstroke, amounts: List[MetricAmount]):
        self.nstroke = nstroke
        self.amounts = amounts

class MetricData:
    def __init__(self, metrics: List[Metric], kb: Keyboard):
        for metric in metrics:
            # I have no idea why these become tuples but they do so I fix it here 
            metric.ngram_type = metric.ngram_type[0]
            metric.predicate = metric.predicate[0]
            metric.value = metric.value[0]

        self.metrics = metrics
        self.strokes = []

        bimetrics = [(idx, m) for (idx, m) in enumerate(metrics) if m.ngram_type in [NgramType.BIGRAM, NgramType.SKIPGRAM]]
        trimetrics = [(idx, m) for (idx, m) in enumerate(metrics) if m.ngram_type == NgramType.TRIGRAM]

        for size in [2, 3]:
            for nstroke in itertools.product(enumerate(kb.keys), repeat=size):
                kind = NstrokeType.TRISTROKE if size == 3 else NstrokeType.BISTROKE
                ns = [pair[0] for pair in nstroke] # real nstroke being the indexes of keys
                keys = [pair[1] for pair in nstroke] # key data for metrics
                data = NstrokeData(Nstroke(kind, ns), [])
                for idx, m in bimetrics if size == 2 else trimetrics:
                    a = keys[0]
                    b = keys[1]
                    is_static_val = isinstance(m.value, int)
                    matches = False
                    value = False
                    if size == 2:
                        matches = m.predicate(a, b)
                        value = m.value(a, b) if not is_static_val else False
                    else:
                        c = keys[2]
                        matches = m.predicate(a, b, c)
                        value = m.value(a, b, c) if not is_static_val else False
                    if not matches:
                        continue
                    if not value:
                        value = m.value
                    data.amounts.append(MetricAmount(idx, value))
                if data.amounts:
                    self.strokes.append(data)

ansi = Keyboard([])
for col in range(10):
    for row in range(3):
        stagger = 0
        if row == 1:
            stagger = 0.25
        elif row == 2:
            stagger = 0.75
        if col == 4:
            finger = Finger.LI
        elif col == 5:
            finger = Finger.RI
        else:
            finger = Finger(col)
        key = KeyCoord(Pos(col, row, 0), stagger+col, row, finger)
        print(key.pos.col, key.pos.row, key.x, key.y, key.finger)
        ansi.keys.append(key)

data = MetricData(base.METRIC_LIST, ansi)
for stroke in data.strokes:
    print(stroke.nstroke.nstroke, [(data.metrics[amt.metric].short, amt.amount) for amt in stroke.amounts])
json_string = json.dumps(ansi, cls=KeymeowEncoder)
# print(json_string)

#generate_metrics(ansi, base.METRIC_LIST)
