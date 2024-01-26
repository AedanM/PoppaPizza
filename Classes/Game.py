"""Class for Game"""
import pygame
from Classes import GameClock, Settings, Inventory
from Definitions import Chances, AssetLibrary

std_dimensions = {"Medium": (1200, 800), "Small": (600, 400), "Large": (2400, 1600)}


class Game:
    CharSpriteGroup: pygame.sprite.Group = pygame.sprite.Group()
    BackgroundSpriteGroup: pygame.sprite.Group = pygame.sprite.Group()
    ForegroundSpriteGroup: pygame.sprite.Group = pygame.sprite.Group()
    SpriteGroups: list = [BackgroundSpriteGroup, CharSpriteGroup, ForegroundSpriteGroup]
    WorkerList: list = []
    CustomerList: list = []
    JobList: list = []
    UserInventory: Inventory.Inventory = None
    ShowScreen: bool = True
    GameClock = GameClock.GameClock(clock=pygame.time.Clock())
    Running: bool = True

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
            str(self.GameClock.DateTime + MoneyText), True, foreColor, backColor
        )
        textrect = text.get_rect()
        textrect.x = locationTopLeft[0]
        textrect.y = locationTopLeft[1]
        self.Screen.blit(source=text, dest=textrect)

    def DrawBackground(self) -> None:
        bg = pygame.image.load(AssetLibrary.ImagePath.BackgroundPath)
        self.Screen.blit(source=bg, dest=(0, 0))

    def RemoveObjFromSprite(self, targetSprite) -> None:
        responseDict = self.MatchIdToPerson(inputId=targetSprite.CorrespondingID)
        if "customer" in responseDict.keys():
            self.CustomerList.remove(responseDict["customer"])
        elif "worker" in responseDict.keys():
            self.WorkerList.remove(responseDict["worker"])
        targetSprite.kill()

    def UpdateSprites(self) -> None:
        for group in self.SpriteGroups:
            group.update()
            for sprite in group:
                sprite.UpdateSprite()
            group.draw(self.Screen)

    @property
    def ScreenSize(self) -> tuple[int, int]:
        return (self.Screen.get_width(), self.Screen.get_height())

    def MatchIdToPerson(self, inputId, targetOutput="all") -> dict:
        output = {}
        if inputId != 0:
            for sprite in self.CharSpriteGroup:
                if sprite.CorrespondingID == inputId:
                    output["sprite"] = sprite
            for worker in self.WorkerList:
                if worker.IdNum == inputId:
                    output["worker"] = worker
            for customer in self.CustomerList:
                if customer.IdNum == inputId:
                    output["customer"] = customer
            return output if targetOutput == "all" else output[targetOutput]
        return None


MasterGame = Game()
