"""Test Module for Game Functions"""

# pylint: disable=invalid-name
from Definitions.DefinedLocations import StandardDimensions
from Engine import Game


def test_ScreenSize() -> None:
    for _, size in StandardDimensions.items():
        currentGame = Game.Game(activateScreen=True, size=size, name="Test")
        assert currentGame.ScreenSize == size
