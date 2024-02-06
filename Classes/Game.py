"""Class for Game"""

import pygame

from Classes import Game, GameClock, Inventory, Settings, Writing
from Definitions import AssetLibrary, Chances, DefinedLocations


class Game:
    CharSpriteGroup: pygame.sprite.Group = pygame.sprite.Group()
    BackgroundSpriteGroup: pygame.sprite.Group = pygame.sprite.Group()
    ForegroundSpriteGroup: pygame.sprite.Group = pygame.sprite.Group()
    SpriteGroups: list = [BackgroundSpriteGroup, CharSpriteGroup, ForegroundSpriteGroup]
    WorkerList: list = []
    CustomerList: list = []
    JobList: list = []
    ButtonList: list = []
    UserInventory: Inventory.Inventory = None
    ShowScreen: bool = True
    GameClock = GameClock.GameClock(clock=pygame.time.Clock())
    Running: bool = True

    def __init__(
        self, activateScreen=True, size=DefinedLocations.LocationDefs.ScreenSize
    ) -> None:
        pygame.init()
        self.Settings = Settings.GameSettings
        self.Chances = Chances.LuckChances()
        self.StartTime = pygame.time.get_ticks()
        self.ShowScreen = activateScreen
        self.UserInventory = Inventory.Inventory()
        if self.ShowScreen:
            self.StartScreen(size=size)

    def StartScreen(self, size) -> None:
        if isinstance(size, str):
            DefinedLocations.LocationDefs.ScreenSize = (
                DefinedLocations.StandardDimensions[size]
            )
            width, height = DefinedLocations.LocationDefs.ScreenSize
        else:
            width, height = size
            DefinedLocations.LocationDefs.ScreenSize = (width, height)
        self.Screen = pygame.display.set_mode(size=(width, height))
        pygame.display.set_caption(title="Poppa Pizza Clone")

        self.Font = pygame.font.Font(None, 36)

    def WriteAllText(self) -> None:
        Writing.WriteButtonLabel(activeGame=self)
        Writing.WriteDateLabel(activeGame=self)

    def DrawBackground(self) -> None:
        bg = pygame.image.load(AssetLibrary.ImagePath.BackgroundPath)
        self.Screen.blit(source=bg, dest=(0, 0))

    def UpdateSprites(self) -> None:
        for group in self.SpriteGroups:
            group.update()
            for sprite in group:
                sprite.UpdateSprite()
            group.draw(self.Screen)

    @property
    def ScreenSize(self) -> tuple[int, int]:
        return (self.Screen.get_width(), self.Screen.get_height())


MasterGame = Game()
