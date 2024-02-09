import time

import pygame

from Definitions import ColorTools, DefinedLocations
from Utilities import Utils


class LightingEffects:

    CurrentNightTransitionAlpha: int = 0
    MaxNightLightAlpha: float = 200
    MaxTransitionCover: float = 0.15
    NightTransitionCover: float = 0.0
    NightTransitionStart: int = 12 * 60

    NightColorOptions: list = {
        "Midnight Blue": ColorTools.DarkBlue,
        "Dusty Orange": ColorTools.BurntOrange,
    }
    NightTransitionColor: ColorTools.Color = NightColorOptions["Midnight Blue"]
    MorningTransitionColor: ColorTools.Color = ColorTools.BlueMorning

    def AllDayBlend(self, gameClock, screenSize) -> None:
        dayPercent = gameClock.DayPercentage
        morningPercent = Utils.Bind(val=1 - (dayPercent), inRange=(0, 1))
        nightPercent = Utils.Bind(val=(dayPercent), inRange=(0, 1))

        currentColor = ColorTools.Color(
            h=(
                (self.MorningTransitionColor.H * morningPercent)
                + (self.NightTransitionColor.H * nightPercent)
            ),
            s=(self.MorningTransitionColor.S * morningPercent)
            + (self.NightTransitionColor.S * nightPercent),
            v=(self.MorningTransitionColor.V * morningPercent)
            + (self.NightTransitionColor.V * nightPercent),
        )
        dayColorScreen = pygame.Surface(screenSize)
        dayColorScreen.fill(currentColor.RGB)
        return dayColorScreen

    def UpdateNightTransition(self, gameClock) -> None:
        if gameClock.Minute > self.NightTransitionStart:
            nightLight = self.MaxNightLightAlpha * (
                (gameClock.Minute - self.NightTransitionStart)
                / (((gameClock.WorkingDayEnd * 60) - self.NightTransitionStart))
            )
        else:
            nightLight = 0

        self.CurrentNightTransitionAlpha = Utils.Bind(
            val=nightLight,
            inRange=(
                0,
                self.MaxNightLightAlpha,
            ),
        )
        self.NightTransitionCover = Utils.ProRateValue(
            value=self.CurrentNightTransitionAlpha,
            inRange=(0, 255),
            outRange=(0, self.MaxTransitionCover),
        )

    def ChangeNightColor(self, rgb) -> None:
        if rgb != (-1, -1, -1):
            r, g, b = rgb
            self.NightTransitionColor = ColorTools.Color(r=r, g=g, b=b)

    def LightingEngine(self, activeGame) -> None:
        lightLayer = self.AllDayBlend(
            gameClock=activeGame.GameClock, screenSize=activeGame.ScreenSize
        )
        activeGame.Screen.blit(
            lightLayer,
            (0, 0),
            special_flags=(pygame.BLEND_ADD),
        )

    def GenerateNightWindows(self) -> None:
        pass

    def GenerateNightTransition(self, screenSize) -> None:
        nightLightScreen = pygame.Surface(screenSize)
        nightLightScreen.fill(self.NightTransitionColor.RGB)
        nightLightScreen.set_alpha(self.CurrentNightTransitionAlpha)
        mask = pygame.Surface(
            Utils.ScaleTuple(tupleArg=screenSize, scale=(1 - self.NightTransitionCover))
        )
        mask.set_alpha(255)
        nightLightScreen.blit(
            mask,
            Utils.ScaleTuple(
                tupleArg=screenSize,
                scale=(self.NightTransitionCover * self.NightTransitionCover),
            ),
        )
        return nightLightScreen
