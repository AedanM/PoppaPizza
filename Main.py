"""Main Body of Game"""

import argparse
import os

# *OS Call used to prevent a time printout from Pygame on first import
# pylint: disable=wrong-import-position
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "True"
import threading
import time

import pygame

from Classes import GameBase, MiniGames
from Definitions import AssetLibrary, ColorDefines, CustomEvents
from Handlers import EventHandler


def Main() -> None:
    """Main Loop of Game"""
    debugFlag = True
    profileFlag = True
    GameBase.MasterGame = GameBase.MainGame()
    pygame.event.post(CustomEvents.UpdateBackground)
    # Enables a series of functions to run automatically
    if profileFlag:
        startTime = time.time()
        GameBase.MasterGame.Settings.CapFrames = False
    if debugFlag:
        EventHandler.DebugSetup()
    while True:
        # try:
        if GameBase.MasterGame.Running:
            match GameBase.MasterGame.Mode:
                case MiniGames.GameMode.Base:
                    EventHandler.MainEventHandler(activeGame=GameBase.MasterGame)
                    GameBase.MasterGame.DrawBackground(source=AssetLibrary.Background)
                    GameBase.MasterGame.UpdateSprites()
                    GameBase.MasterGame.WriteAllText()
                    GameBase.MasterGame.UpdateLightingEngine()
                case MiniGames.GameMode.TriviaGame:
                    GameBase.MasterGame.DrawBackground(
                        source=AssetLibrary.TriviaBackground
                    )
                    GameBase.MasterGame.MiniGame.PlayGame(
                        activeGame=GameBase.MasterGame
                    )
                    EventHandler.TriviaEventHandler(activeGame=GameBase.MasterGame)

        if GameBase.MasterGame.ShowScreen:
            pygame.display.update()

        # Control the frame rate
        GameBase.MasterGame.GameClock.UpdateClock(
            clockSpeed=GameBase.MasterGame.Settings.ClockSpeed,
            frameCap=GameBase.MasterGame.Settings.CapFrames,
        )
        if profileFlag and (time.time() - startTime > 30):
            break
    # except Exception as e:
    # print(f"{e} Occured")


if __name__ == "__main__":
    Main()
