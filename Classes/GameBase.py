"""Class for Game"""

from typing import Any

import pygame

from Classes import GameClock, GameLighting, Inventory, MiniGames, Settings, Writing
from Definitions import AssetLibrary, Chances, CustomEvents, Restaurants
from Definitions.DefinedLocations import LocationDefs, StandardDimensions
from Engine import Color, Game, RoundBasedGame


class MainGame(Game.Game):
    """Master class for all elements in Game"""

    CharSpriteGroup: pygame.sprite.Group = pygame.sprite.Group()
    BackgroundSpriteGroup: pygame.sprite.Group = pygame.sprite.Group()
    ForegroundSpriteGroup: pygame.sprite.Group = pygame.sprite.Group()
    WorkerList: list = []
    CustomerList: list = []
    JobList: list = []
    ButtonList: list = []
    UserInventory: Inventory.Inventory = None  # type: ignore
    Mode: MiniGames.GameMode = MiniGames.GameMode.Base
    MiniGame: RoundBasedGame.RoundBasedGame = None  # type: ignore

    def __init__(self, activateScreen=True, size=LocationDefs.ScreenSize) -> None:
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
            LocationDefs.ScreenSize = StandardDimensions[size]
            width, height = LocationDefs.ScreenSize
        else:
            width, height = size
            LocationDefs.ScreenSize = (width, height)
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
        self, source: pygame.Surface = None, color: Color.Color = None  # type: ignore
    ) -> None:
        """Wiping screen with background image"""
        if source:
            self.Screen.blit(source=source, dest=(0, 0))
        elif color:
            self.Screen.fill(color.RGB)
        else:
            super().DrawBackground()

    def ClearMiniGame(self) -> None:
        self.MiniGame = None  # type: ignore
        self.Mode = MiniGames.GameMode.Base
        self.GameClock.SetRunning(True)

    def UpdateLightingEngine(self) -> None:
        self.Lighting.LightingEngine(activeGame=self, dayTransition=True)

    @property
    def HasGameOver(self) -> str:
        if super().HasGameOver:
            return super().HasGameOver
        if self.UserInventory.Money < 0:
            return "Ran Out of Cash"
        return ""

    def MakeSaveObj(self) -> dict[str, Any]:
        saveDict = super().MakeSaveObj()
        saveDict["Workers"] = self.WorkerList
        saveDict["Customers"] = self.CustomerList
        saveDict["Jobs"] = self.JobList
        saveDict["Restuarants"] = Restaurants.RestaurantList
        saveDict["Inventory"] = self.UserInventory
        return saveDict

    def LoadSaveObj(self, saveDict) -> None:
        super().LoadSaveObj(saveDict=saveDict)
        self.WorkerList = saveDict["Workers"]
        self.CustomerList = saveDict["Customers"]
        self.JobList = saveDict["Jobs"]
        Restaurants.RestaurantList = saveDict["Restuarants"]
        self.UserInventory = saveDict["Inventory"]

    def LoadGame(self) -> None:
        super().LoadGame()
        pygame.event.post(CustomEvents.UpdateBackground)


MasterGame = MainGame()
