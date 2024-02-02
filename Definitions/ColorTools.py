"""Class for Altering Colors"""
import colorsys
from dataclasses import dataclass

import numpy as np

from Utilities import Utils


@dataclass
class Color:
    H: int
    S: int
    V: int

    def __init__(self, h, s, v) -> None:
        self.H = Utils.Bind(val=h, inRange=(0, 255))
        self.S = Utils.Bind(val=s, inRange=(0, 255))
        self.V = Utils.Bind(val=v, inRange=(0, 255))

    def GetNumPy(self) -> "np.NDArray[np.uint8]":
        return np.array([self.H, self.S, self.V], dtype=np.uint8)

    @property
    def HSV(self) -> tuple[int, int, int]:
        return (self.H, self.S, self.V)

    @property
    def RGB(self) -> tuple[int, ...]:
        return tuple(
            round(i * 255)
            for i in colorsys.hsv_to_rgb(
                float(
                    self.H,
                )
                / 255,
                float(self.S) / 255,
                float(self.V) / 255,
            )
        )

    @property
    def BGR(self) -> tuple[int, int, int]:
        rgb = self.RGB
        return (rgb[2], rgb[1], rgb[0])


White = Color(h=0, s=0, v=255)
Blue = Color(h=150, s=200, v=128)
Green = Color(h=70, s=200, v=128)
LimeGreen = Color(h=70, s=200, v=255)
Red = Color(h=0, s=200, v=255)
Grey = Color(h=0, s=0, v=200)
Pink = Color(h=220, s=200, v=128)
Yellow = Color(h=25, s=200, v=180)
CautionTapeYellow = Color(h=37, s=255, v=255)
Brown = Color(h=29, s=230, v=100)
Black = Color(h=0, s=0, v=0)
