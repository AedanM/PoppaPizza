"""Test Module for Settings"""

# pylint: disable=invalid-name

from Classes import GameBase


def test_ClockSpeed() -> None:
    assert GameBase.MasterGame.Settings is not None
