"""Class for Game"""
import pygame
from Classes import Chances, GameClock
from Classes.Sprite import ImagePaths

iPaths = ImagePaths()
std_dimensions = {"Medium": (1200, 800), "Small": (600, 400), "Large": (2400, 1600)}


class Game:
    ActiveTimerBars: list = []
    CharSpriteGroup: pygame.sprite.Group = pygame.sprite.Group()
    BackgroundSpriteGroup: pygame.sprite.Group = pygame.sprite.Group()
    SpriteGroups: list = [BackgroundSpriteGroup, CharSpriteGroup]
    LineList: list = [(-1, -1), (1, 1)]
    WorkerList: list = []
    CustomerList: list = []
    JobList: list = []
    Money: int = 0
    TimerBars: list = []
    ShowScreen: bool = True
    Clock: GameClock = GameClock.GameClock(clock=pygame.time.Clock())

    def __init__(self, activateScreen=True, size=std_dimensions["Medium"]) -> None:
        pygame.init()
        self.Chances = Chances.LuckChances()
        self.StartTime = pygame.time.get_ticks()
        self.ShowScreen = activateScreen
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

    def DrawScreenClock(self, locationTopLeft, foreColor, backColor) -> None:
        text = self.Font.render(str(self.Clock.DateTime), True, foreColor, backColor)
        textrect = text.get_rect()
        textrect.x = locationTopLeft[0]
        textrect.y = locationTopLeft[1]
        self.Screen.blit(source=text, dest=textrect)

    def DrawBackground(self) -> None:
        bg = pygame.image.load(iPaths.BackgroundPath)
        self.Screen.blit(source=bg, dest=(0, 0))

    def RemoveObj(self, targetSprite) -> None:
        targetSprite.kill()
        self.CustomerList = [
            x for x in self.CustomerList if x.IdNum != targetSprite.CorrespondingID
        ]
        self.WorkerList = [
            x for x in self.WorkerList if x.IdNum != targetSprite.CorrespondingID
        ]

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
        return (self.Screen.get_width(), self.Screen.get_width())


MasterGame = None
