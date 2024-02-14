from Engine import Utils


import numpy as np


import colorsys
from dataclasses import dataclass


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
            raise Exception(f"Invalid Inputs: {e}") from e

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
