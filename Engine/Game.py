import pygame

from Engine import Clock, Color, LightingEngine


class Game:
    Name: str
    SpriteGroups: list = []
    GameClock = Clock.Clock(clock=pygame.time.Clock())
    ShowScreen: bool = True
    Running: bool = True
    BackgroundColor: Color.Color = Color.Color(hexstring="#000000")
    Lighting: LightingEngine.LightingEngine = None

    def __init__(self, size, name, activateScreen=True) -> None:
        pygame.init()
        self.StartTime = pygame.time.get_ticks()
        self.ShowScreen = activateScreen
        self.Name = name
        if self.ShowScreen:
            self.StartScreen(size=size)

    def StartScreen(self, size) -> None:
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
