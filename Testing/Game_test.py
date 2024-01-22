from telnetlib import GA
from Classes import Game


def test_ScreenSize() -> None:
    for key, size in Game.std_dimensions.items():
        Game.MasterGame = Game.Game(activateScreen=True, size=size)
        assert Game.MasterGame.ScreenSize == size


def RunAllGameTests() -> bool:
    test_ScreenSize()
    return True
