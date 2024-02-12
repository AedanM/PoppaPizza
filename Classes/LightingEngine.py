import time

import pygame

from Definitions import AssetLibrary, ColorTools, DefinedLocations
from Utilities import Utils


class LightingEffects:
    CurrentNightTransitionAlpha: int = 0
    MaxNightLightAlpha: float = 200
    NightTransitionCover: float = 0.05
    LightMask: pygame.Surface = pygame.image.load(AssetLibrary.ImagePath.LightMaskPath)

    MorningColorOptions: list = {
        "Blue": ColorTools.Blue,
        "Orange": ColorTools.OrangeMorning,
    }
    NightColorOptions: list = {
        "Blue": ColorTools.Blue,
        "Orange": ColorTools.OrangeNight,
    }
    NightTransitionColor: ColorTools.Color = NightColorOptions["Orange"]
    MorningTransitionColor: ColorTools.Color = MorningColorOptions["Orange"]

    def AllDayBlend(self, gameClock, screenSize) -> None:
        dayPercent = gameClock.DayPercentage
        morningPercent = Utils.Bind(val=1 - (dayPercent * 2), inRange=(0, 1))
        nightPercent = Utils.Bind(val=((dayPercent - 0.5) * 2), inRange=(0, 1))
        noonPercent = (1 - morningPercent) - nightPercent
        currentColor = ColorTools.Color(
            h=(self.MorningTransitionColor.H * morningPercent)
            + (self.NightTransitionColor.H * nightPercent),
            s=(self.MorningTransitionColor.S * morningPercent)
            + (self.NightTransitionColor.S * nightPercent),
            v=(self.MorningTransitionColor.V * morningPercent)
            + (self.NightTransitionColor.V * nightPercent)
            + (ColorTools.White.V * noonPercent),
        )
        dayColorScreen = pygame.Surface(screenSize)
        dayColorScreen.fill(currentColor.RGB)
        return dayColorScreen

    def ChangeNightColor(self, rgb) -> None:
        if rgb != (-1, -1, -1):
            r, g, b = rgb
            self.NightTransitionColor = ColorTools.Color(r=r, g=g, b=b)

    def LightingEngine(self, activeGame) -> None:
        lightLayer = self.AllDayBlend(
            gameClock=activeGame.GameClock, screenSize=activeGame.ScreenSize
        )
        lightLayer.blit(
            self.LightMask,
            (0, 0),
            special_flags=(pygame.BLEND_ADD),
        )
        activeGame.Screen.blit(
            lightLayer,
            (0, 0),
            special_flags=(pygame.BLEND_MULT),
        )
