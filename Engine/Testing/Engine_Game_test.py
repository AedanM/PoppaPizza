"""Test Module for Game Functions"""

# pylint: disable=invalid-name
from Engine import Game


def test_ScreenSize() -> None:
    for _, size in Game.StandardDimensions.items():
        currentGame = Game.Game(activateScreen=True, size=size, name="Test")
        assert currentGame.ScreenSize == size
