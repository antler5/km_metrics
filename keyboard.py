from enum import Enum
from typing import Dict, List

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

class Hand(Enum):
    LEFT = 0
    RIGHT = 1

class FingerKind(Enum):
    PINKY = 0
    RING = 1
    MIDDLE = 2
    INDEX = 3
    THUMB = 4

def hand(f: Finger) -> Hand:
    if f.value <= 4:
        return Hand.LEFT
    else:
        return Hand.RIGHT

def kind(f: Finger) -> FingerKind:
    if f.value <= 4:
        return FingerKind(f.value),
    else:
        return FingerKind(9 - f.value)

class Pos:
    def __init__(self, row: int, col: int, layer: int):
        self.row = row
        self.col = col
        self.layer = layer
    
class KeyCoord:
    def __init__(self, pos: Pos, x: float, y: float, finger: Finger):
        self.pos = pos
        self.x = x
        self.y = y
        self.finger = finger
        
class Keyboard:
    def __init__(self, finger_map: Dict[Finger, List[KeyCoord]]):
        self.finger_map = finger_map
        
