from enum import Enum
from typing import Dict, List

class Hand(Enum):
    LEFT = 0
    RIGHT = 1

class FingerKind(Enum):
    PINKY = 0
    RING = 1
    MIDDLE = 2
    INDEX = 3
    THUMB = 4

class Finger(Enum):
    LP = 0
    LR = 1
    LM = 2
    LI = 3
    LT = 4
    RT = 5
    RI = 6
    RM = 7
    RR = 8
    RP = 9

    def hand(self) -> Hand:
        if self.value <= 4:
            return Hand.LEFT
        else:
            return Hand.RIGHT

    def kind(self) -> FingerKind:
        if self.value <= 4:
            return FingerKind(self.value)
        else:
            return FingerKind(9 - self.value)

class Pos:
    def __init__(self, col: int, row: int, layer: int):
        self.col = col
        self.row = row
        self.layer = layer
    
class KeyCoord:
    def __init__(self, pos: Pos, x: float, y: float, finger: Finger):
        self.pos = pos
        self.x = x
        self.y = y
        self.finger = finger
        
class Keyboard:
    def __init__(self, name: str, keymap: List[List[KeyCoord]]):
        self.name = name
        self.keymap = keymap
        self.combos = []

    def compound_nstrokes(self):
        """Returns a flattened list of nstrokes including combos"""
        base = itertools.chain.from_iterable(self.keymap)
        combined = itertools.chain(base, self.combos)
        return combined
