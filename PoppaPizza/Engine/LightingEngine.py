"""Custom Lighting Engine to overlay effects"""

import pygame

from Engine import Color, Utils


class LightingEngine:
    CurrentNightTransitionAlpha: int = 0
    MaxNightLightAlpha: float = 200
    NightTransitionCover: float = 0.05
    LightMask: pygame.Surface = pygame.Surface((1, 1))
    DayColorScreen: pygame.Surface = pygame.Surface((1, 1))
    NightTransitionColor: Color.Color = Color.Color(hexstring="#FFFFFF")
    MorningTransitionColor: Color.Color = Color.Color(hexstring="#000000")

    def __init__(self, screenSize: tuple[int, int]) -> None:
        self.DayColorScreen = pygame.Surface(screenSize)

    def AllDayBlend(self, gameClock) -> pygame.Surface:
        dayPercent = gameClock.DayPercentage
        morningPercent = Utils.Bind(val=1 - (dayPercent * 2), inRange=(0, 1))
        nightPercent = Utils.Bind(val=((dayPercent - 0.5) * 2), inRange=(0, 1))
        noonPercent = (1 - morningPercent) - nightPercent
        currentColor = Color.Color(
            h=int(
                (self.MorningTransitionColor.H * morningPercent)
                + (self.NightTransitionColor.H * nightPercent)
            ),
            s=int(
                (self.MorningTransitionColor.S * morningPercent)
                + (self.NightTransitionColor.S * nightPercent)
            ),
            v=int(
                (self.MorningTransitionColor.V * morningPercent)
                + (self.NightTransitionColor.V * nightPercent)
                + (255 * noonPercent)
            ),
        )
        self.DayColorScreen.fill(currentColor.RGB)
        return self.DayColorScreen

    def ChangeNightColor(self, rgb: tuple[int, int, int]) -> None:
        if rgb != (-1, -1, -1):
            r, g, b = rgb
            self.NightTransitionColor = Color.Color(r=r, g=g, b=b)

    def LightingEngine(self, activeGame, dayTransition=False) -> None:
        if dayTransition:
            lightLayer = self.AllDayBlend(gameClock=activeGame.GameClock)
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
