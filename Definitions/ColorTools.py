"""Class for Altering Colors"""

import colorsys
from dataclasses import dataclass

import numpy as np

from Utilities import Utils


def RGB_to_HSV(red, green, blue) -> None:
    red_percentage = red / float(255)
    green_percentage = green / float(255)
    blue_percentage = blue / float(255)
    color_hsv_percentage = colorsys.rgb_to_hsv(
        red_percentage, green_percentage, blue_percentage
    )

    h = round(255 * color_hsv_percentage[0])
    s = round(255 * color_hsv_percentage[1])
    v = round(255 * color_hsv_percentage[2])

    return h, s, v


@dataclass
class Color:
    """Class for Defined Colors"""

    H: int
    S: int
    V: int

    def __init__(
        self, h=None, s=None, v=None, r=None, g=None, b=None, hexstring=None
    ) -> None:
        """Creates a color from HSV or RGB input"""
        try:
            if h is not None and s is not None and v is not None:
                self.H = Utils.Bind(val=h, inRange=(0, 255))
                self.S = Utils.Bind(val=s, inRange=(0, 255))
                self.V = Utils.Bind(val=v, inRange=(0, 255))
            elif r is not None and g is not None and b is not None:
                self.H, self.S, self.V = RGB_to_HSV(red=r, green=g, blue=b)
            elif hexstring is not None:
                hexstring = hexstring.replace("0x", "").replace("#", "")
                self.H, self.S, self.V = RGB_to_HSV(
                    red=int(hexstring[0:1], 16) * (256 / 16),
                    green=int(hexstring[2:3], 16) * (256 / 16),
                    blue=int(hexstring[4:5], 16) * (256 / 16),
                )
            else:
                raise Exception("Invalid Inputs")
        except Exception as e:
            raise Exception(f"Invalid Inputs: {e}")

    def GetNumPy(self) -> "np.NDArray[np.uint8]":
        """Numpy Representation"""
        return np.array([self.H, self.S, self.V], dtype=np.uint8)

    @property
    def HSV(self) -> tuple[int, int, int]:
        """HSV Representation"""
        return (self.H, self.S, self.V)

    @property
    def RGB(self) -> tuple[int, ...]:
        """RGB Representation"""
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
        """BGR Representation"""
        rgb = self.RGB
        return (rgb[2], rgb[1], rgb[0])

    @property
    def HexString(self) -> str:
        """Returns the hex string representation"""
        R, G, B = self.RGB
        return f"#{R:2x}{G:2x}{B:2x}"


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
OrangeMorning = Color(h=15, s=50, v=255)
OrangeNight = Color(h=15, s=130, v=200)
BlueMorning = Color(h=200, s=50, v=255)
BlueNight = Color(h=200, s=130, v=200)
