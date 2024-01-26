from Definitions import ColorTools
import numpy as np


def test_ColorClass() -> None:
    newColor = ColorTools.Color(H=237, S=185, V=128)
    assert newColor.RGB == (128, 35, 74)
    assert newColor.HSV == (237, 185, 128)
    assert newColor.BGR == (74, 35, 128)
    assert newColor.GetNumPy().all() == np.array([237, 185, 128], dtype=np.uint8).all()
