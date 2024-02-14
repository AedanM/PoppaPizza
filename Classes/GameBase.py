"""Class for Game"""

import pygame

from Classes import (
    GameBase,
    GameClock,
    GameLighting,
    Inventory,
    MiniGames,
    Settings,
    Writing,
)
from Definitions import AssetLibrary, Chances, DefinedLocations
from Engine import Color, Game, RoundBasedGame

# TODO - extract a parent class for a general framework


class MainGame(Game.Game):
    """Master class for all elements in Game"""

    CharSpriteGroup: pygame.sprite.Group = pygame.sprite.Group()
    BackgroundSpriteGroup: pygame.sprite.Group = pygame.sprite.Group()
    ForegroundSpriteGroup: pygame.sprite.Group = pygame.sprite.Group()
    WorkerList: list = []
    CustomerList: list = []
    JobList: list = []
    ButtonList: list = []
    UserInventory: Inventory.Inventory = None
    Mode: MiniGames.GameMode = MiniGames.GameMode.Base
    MiniGame: RoundBasedGame.RoundBasedGame = None

    def __init__(
        self, activateScreen=True, size=DefinedLocations.LocationDefs.ScreenSize
    ) -> None:
        """Init for Game

        Args-
            activateScreen (bool, optional): Is the screen turned on. Defaults to True.
            size (tuple, optional): Dimensions of Screeen. Defaults to DefinedLocations.LocationDefs.ScreenSize.
        """
        super().__init__(
            name="Poppa Pizza",
            activateScreen=activateScreen,
            size=size,
        )
        self.SpriteGroups = [
            self.BackgroundSpriteGroup,
            self.CharSpriteGroup,
            self.ForegroundSpriteGroup,
        ]
        self.GameClock = GameClock.GameClock(clock=pygame.time.Clock())
        self.Settings = Settings.GameSettings
        self.Chances = Chances.LuckChances()
        self.UserInventory = Inventory.Inventory()
        self.Lighting = GameLighting.GameLighting(screenSize=size)

        self.ConvertPreRendered()

    def StartScreen(self, size) -> None:
        if isinstance(size, str):
            DefinedLocations.LocationDefs.ScreenSize = (
                DefinedLocations.StandardDimensions[size]
            )
            width, height = DefinedLocations.LocationDefs.ScreenSize
        else:
            width, height = size
            DefinedLocations.LocationDefs.ScreenSize = (width, height)
        super().StartScreen(size=size)

    def ConvertPreRendered(self) -> None:
        """Speeds up blitting by converting colorspaces"""
        AssetLibrary.Background = AssetLibrary.Background.convert()
        AssetLibrary.TriviaBackground = AssetLibrary.TriviaBackground.convert()
        self.Lighting.LightMask = self.Lighting.LightMask.convert()

    def WriteAllText(self) -> None:
        """Write all text visible in game"""
        Writing.WriteButtonLabel(activeGame=self)
        Writing.WriteDateLabel(activeGame=self)
        Writing.WriteKitchenLabel(activeGame=self)

    def DrawBackground(
        self, source: pygame.Surface = None, color: Color.Color = None
    ) -> None:
        """Wiping screen with background image"""
        if source:
            self.Screen.blit(source=source, dest=(0, 0))
        elif color:
            self.Screen.fill(color.RGB)
        else:
            super().DrawBackground()

    def ClearMiniGame(self) -> None:
        self.MiniGame = None
        self.Mode = MiniGames.GameMode.Base
        self.GameClock.SetRunning(True)

    def UpdateLightingEngine(self) -> None:
        self.Lighting.LightingEngine(activeGame=self, dayTransition=True)


MasterGame = MainGame()
