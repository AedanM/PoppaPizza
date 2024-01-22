"""Class for Game"""
import pygame
from Assets import AssetLibrary
from Classes import Chances, GameClock, Settings
from Assets import AssetLibrary
import Classes.Inventory as Inventory

std_dimensions = {"Medium": (1200, 800), "Small": (600, 400), "Large": (2400, 1600)}


class Game:
    ImageTypes = AssetLibrary.ImageTypes
    ImagePath = AssetLibrary.ImagePaths()
    PathToTypeDict: dict = AssetLibrary.PathToTypeDict
    ActiveTimerBars: list = []
    CharSpriteGroup: pygame.sprite.Group = pygame.sprite.Group()
    BackgroundSpriteGroup: pygame.sprite.Group = pygame.sprite.Group()
    SpriteGroups: list = [BackgroundSpriteGroup, CharSpriteGroup]
    LineList: list = [(-1, -1), (1, 1)]
    WorkerList: list = []
    CustomerList: list = []
    JobList: list = []
    UserInventory: Inventory.Inventory = None
    TimerBars: list = []
    ShowScreen: bool = True
    Clock: GameClock = GameClock.GameClock(clock=pygame.time.Clock())

    def __init__(self, activateScreen=True, size=std_dimensions["Medium"]) -> None:
        pygame.init()
        self.Settings = Settings.GameSettings
        self.Chances = Chances.LuckChances()
        self.StartTime = pygame.time.get_ticks()
        self.ShowScreen = activateScreen
        self.UserInventory = Inventory.Inventory()
        if self.ShowScreen:
            self.StartScreen(size=size)

    def StartScreen(self, size) -> None:
        if type(size) == std_dimensions:
            width, height = std_dimensions[size]
        else:
            width, height = size
        self.Screen = pygame.display.set_mode(size=(width, height))
        pygame.display.set_caption(title="Poppa Pizza Clone")

        self.Font = pygame.font.Font(None, 36)

    def DrawScreenClock(
        self, locationTopLeft, foreColor, backColor, withMoney=False
    ) -> None:
        MoneyText = f" ${self.UserInventory.Money:0.2f}" if withMoney else ""
        text = self.Font.render(
            str(self.Clock.DateTime + MoneyText), True, foreColor, backColor
        )
        textrect = text.get_rect()
        textrect.x = locationTopLeft[0]
        textrect.y = locationTopLeft[1]
        self.Screen.blit(source=text, dest=textrect)

    def DrawBackground(self) -> None:
        bg = pygame.image.load(self.ImagePath.BackgroundPath)
        self.Screen.blit(source=bg, dest=(0, 0))

    def RemoveObjFromSprite(self, targetSprite) -> None:
        self.CustomerList = [
            x for x in self.CustomerList if x.IdNum != targetSprite.CorrespondingID
        ]
        self.WorkerList = [
            x for x in self.WorkerList if x.IdNum != targetSprite.CorrespondingID
        ]
        targetSprite.kill()

    def UpdateSprites(self) -> None:
        for group in self.SpriteGroups:
            group.update()
            for sprite in group:
                sprite.Update()
            group.draw(self.Screen)

    def UpdateTimers(self) -> None:
        for timer in self.TimerBars:
            timer.UpdateAndDraw()

    @property
    def ScreenSize(self) -> tuple[int, int]:
        return (self.Screen.get_width(), self.Screen.get_height())

    def MatchSpriteToPerson(self, inputId) -> dict:
        output = {}
        for sprite in self.CharSpriteGroup:
            if sprite.CorrespondingID == inputId:
                output["sprite"] = sprite
        for worker in self.WorkerList:
            if worker.IdNum == inputId:
                output["worker"] = worker
        for customer in self.CustomerList:
            if customer.IdNum == inputId:
                output["customer"] = customer
        return output


MasterGame = Game()
