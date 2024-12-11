"""Test Module for ColorTools"""
# pylint: disable=invalid-name
import numpy as np
from Engine import Color


def test_ColorClass() -> None:
    newColor = Color.Color(h=237, s=185, v=128)
    assert newColor.RGB == (128, 35, 74)
    assert newColor.HSV == (237, 185, 128)
    assert newColor.BGR == (74, 35, 128)
    assert newColor.GetNumPy().all() == np.array([237, 185, 128], dtype=np.uint8).all()
