from enum import Enum
class Gearbox():
    class ATMode(Enum):
        M, P, R, N, D, L = range(1, 7)
