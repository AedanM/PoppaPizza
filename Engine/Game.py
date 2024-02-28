"""Base class for pygame engine"""

from typing import Any

import pygame

from Engine import Clock, Color, LightingEngine, SaveHandler


class Game:
    Name: str
    SpriteGroups: list = []
    GameClock = Clock.Clock(clock=pygame.time.Clock())
    ShowScreen: bool = True
    Running: bool = True
    BackgroundColor: Color.Color = Color.Color(hexstring="#000000")
    Lighting: LightingEngine.LightingEngine = None  # type: ignore
    Screen: pygame.Surface = None  # type: ignore

    def __init__(self, size: tuple[int, int], name: str, activateScreen: bool = True) -> None:
        pygame.init()
        self.StartTime = pygame.time.get_ticks()
        self.ShowScreen = activateScreen
        self.Name = name
        if self.ShowScreen:
            self.StartScreen(size=size)

    def StartScreen(self, size: tuple[int, int]) -> None:
        """Begins the screen and sets size

        Args-
            size (str | tuple): Either member of StandardDimensions or custom tuple
        """
        self.Screen = pygame.display.set_mode(size=size, flags=pygame.DOUBLEBUF)
        self.Screen.set_alpha(None)
        pygame.display.set_caption(self.Name)

    def DrawBackground(self):
        self.Screen.fill(self.BackgroundColor.RGB)

    def UpdateSprites(self) -> None:
        """Update each sprite each frame"""
        for group in self.SpriteGroups:
            group.update()
            for sprite in group:
                sprite.UpdateSprite(activeGame=self)
            group.draw(self.Screen)

    def UpdateLightingEngine(self) -> None:
        self.Lighting.LightingEngine(activeGame=self, dayTransition=False)

    @property
    def ScreenSize(self) -> tuple[int, int]:
        """Current size of screen

        Returns-
            tuple: tuple of current Size
        """
        return (self.Screen.get_width(), self.Screen.get_height())

    @property
    def HasGameOver(self) -> str:
        return ""

    def SaveGame(self) -> bool:
        return SaveHandler.SaveGame(saveObj=self.MakeSaveObj(), path="SaveGame.sav")

    def LoadGame(self) -> bool:
        status, saveDict = SaveHandler.LoadGame(path="SaveGame.sav")
        if status:
            self.LoadSaveObj(saveDict=saveDict)
        return status

    def MakeSaveObj(self) -> dict[str, Any]:
        saveDict = {
            "Screen Size": self.ScreenSize,
            "Game Clock": self.GameClock.UnixTime,
        }
        return saveDict

    def LoadSaveObj(self, saveDict: dict):
        self.StartScreen(size=saveDict["Screen Size"])
        self.GameClock.SetUnixTime(time=saveDict["Game Clock"])


StandardDimensions = {"Medium": (1200, 800), "Small": (600, 400), "Large": (2400, 1600)}
