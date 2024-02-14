import pygame

from Definitions import AssetLibrary, ColorDefines
from Engine import Color, LightingEngine


class GameLighting(LightingEngine.LightingEngine):
    MorningColorOptions: list = {
        "Blue": ColorDefines.Blue,
        "Orange": ColorDefines.OrangeMorning,
    }
    NightColorOptions: list = {
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
