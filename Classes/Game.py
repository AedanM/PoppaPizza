import pygame

std_dimensions = {"Medium": (1200, 800), "Small": (600, 400), "Large": (2400, 1600)}


class Game:
    ActiveTimerBars: list = []
    CharSpriteGroup = pygame.sprite.Group()
    BackgroundSpriteGroup = pygame.sprite.Group()
    SpriteGroups: list = [BackgroundSpriteGroup, CharSpriteGroup]
    WorkerList: list = []
    CustomerList: list = []
    JobList: list = []
    Money: int = []

    def __init__(self, size):
        pygame.init()

        self.gameClock = pygame.time.Clock()
        self.startTime = pygame.time.get_ticks()

        width, height = std_dimensions[size]
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Poppa Pizza Clone")

        self.font = pygame.font.Font(None, 36)


MasterGame = Game("Medium")
