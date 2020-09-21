from enum import Enum


class Differential:
    class Type(Enum):
        CLUTCHPACK, LOCKED, OPEN, TORQUEBIAS, VISCOUS = range(1, 6)
