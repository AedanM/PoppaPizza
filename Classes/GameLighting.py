import pygame

from AtomicbritEngine.Engine import Color, LightingEngine
from Definitions import AssetLibrary, ColorDefines


class GameLighting(LightingEngine.LightingEngine):
    MorningColorOptions: dict = {
        "Blue": ColorDefines.Blue,
        "Orange": ColorDefines.OrangeMorning,
    }
    NightColorOptions: dict = {
        "Blue": ColorDefines.Blue,
        "Orange": ColorDefines.OrangeNight,
    }
    LightMask: pygame.Surface = pygame.image.load(AssetLibrary.ImagePath.LightMaskPath)
    NightTransitionColor: Color.Color = NightColorOptions["Orange"]
    MorningTransitionColor: Color.Color = MorningColorOptions["Orange"]

    def __init__(self, screenSize) -> None:
        super().__init__(screenSize=screenSize)
        self.LightMask = self.LightMask.convert()

    def LightingEngine(self, activeGame, dayTransition=False) -> None:
        super().LightingEngine(activeGame=activeGame, dayTransition=dayTransition)
