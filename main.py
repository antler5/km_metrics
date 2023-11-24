import json
import itertools
import os
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
            return {"name": o.name, "keys": {"map": o.keymap}}
        if isinstance(o, Nstroke):
            return o.nstroke
        if isinstance(o, NstrokeType):
            return o.name[0]
        if isinstance(o, NgramType):
            return o.name.capitalize()
        if isinstance(o, NstrokeData):
            return {"ns": o.nstroke, "ams": o.amounts}
        if isinstance(o, Metric):
            return {"name": o.name, "short": o.short, "ngram_type": o.ngram_type}
        if isinstance(o, MetricAmount):
            return {"met": o.metric, "amt": o.amount}
        if isinstance(o, MetricData):
            return {"metrics": o.metrics, "strokes": o.strokes, "keyboard": o.keyboard}

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
        self.metrics = metrics
        self.strokes = []
        self.keyboard = kb

        bimetrics = [(idx, m) for (idx, m) in enumerate(metrics) if m.ngram_type in [NgramType.BIGRAM, NgramType.SKIPGRAM]]
        trimetrics = [(idx, m) for (idx, m) in enumerate(metrics) if m.ngram_type == NgramType.TRIGRAM]

        for size in [2, 3]:
            for nstroke in itertools.product(enumerate(list(itertools.chain.from_iterable(kb.keymap))), repeat=size):
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

from keyboard_metrics import KEYBOARDS

for (k, m) in KEYBOARDS:
    print(f"Exporting {k.name}...", end="")
    data = MetricData(m, k)
    json_string = json.dumps(data, cls=KeymeowEncoder)
    f = open(os.path.join("./export/", k.name + ".json"), "w")
    f.write(json_string)
    f.close()
    print(" done")

#generate_metrics(ansi, base.METRIC_LIST)
