import colorsys
from dataclasses import dataclass

import numpy as np

from Engine import Utils


def RGB_to_HSV(red: int, green: int, blue: int) -> tuple:
    red_percentage = red / float(255)
    green_percentage = green / float(255)
    blue_percentage = blue / float(255)
    color_hsv_percentage = colorsys.rgb_to_hsv(red_percentage, green_percentage, blue_percentage)

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
        self,
        h: int = None,  # type: ignore
        s: int = None,  # type: ignore
        v: int = None,  # type: ignore
        r: int = None,  # type: ignore
        g: int = None,  # type: ignore
        b: int = None,  # type: ignore
        hexstring: str = None,  # type: ignore
    ) -> None:
        """Creates a color from HSV or RGB input"""
        try:
            if h is not None and s is not None and v is not None:
                self.H = int(Utils.Bind(val=h, inRange=(0, 255)))
                self.S = int(Utils.Bind(val=s, inRange=(0, 255)))
                self.V = int(Utils.Bind(val=v, inRange=(0, 255)))
            elif r is not None and g is not None and b is not None:
                self.H, self.S, self.V = RGB_to_HSV(red=r, green=g, blue=b)
            elif hexstring is not None:
                hexstring = hexstring.replace("0x", "").replace("#", "")
                self.H, self.S, self.V = RGB_to_HSV(
                    red=int(int(hexstring[0:1], 16) * (256 / 16)),
                    green=int(int(hexstring[2:3], 16) * (256 / 16)),
                    blue=int(int(hexstring[4:5], 16) * (256 / 16)),
                )
            else:
                raise Exception("Invalid Inputs")
        except Exception as e:
            raise Exception(f"Invalid Inputs: {e}") from e

    def GetNumPy(self) -> "np.NDArray[np.uint8]":  # type: ignore
        """Numpy Representation"""
        return np.array([self.H, self.S, self.V], dtype=np.uint8)

    @property
    def HSV(self) -> tuple[int, int, int]:
        """HSV Representation"""
        return (self.H, self.S, self.V)

    @property
    def RGB(self) -> tuple[int, int, int]:
        """RGB Representation"""
        rawColor = tuple(
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
        return (rawColor[0], rawColor[1], rawColor[2])

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
