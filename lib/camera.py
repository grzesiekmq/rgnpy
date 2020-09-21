from enum import Enum


class Camera:
    class CameraView(Enum):
        BACK, SIDELEFT, SIDERIGHT, NEAR, FAR, DRIVER, FRONT, BUMPER, HOOD = range(1, 10)
