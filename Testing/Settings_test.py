"""Test Module for Settings"""
# pylint: disable=invalid-name

from Classes import Game


def test_ClockSpeed() -> None:
    assert Game.MasterGame.Settings is not None
