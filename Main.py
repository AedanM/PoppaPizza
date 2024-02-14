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
from Definitions import AssetLibrary, CustomEvents
from Handlers import EventHandler

GAME_START_TIME = 0


def MainLoop() -> None:
    """Main Loop of Game"""
    if GameBase.MasterGame.Running:
        match GameBase.MasterGame.Mode:
            case MiniGames.GameMode.Base:
                EventHandler.MainEventHandler(activeGame=GameBase.MasterGame)
                GameBase.MasterGame.DrawBackground(source=AssetLibrary.Background)
                GameBase.MasterGame.UpdateSprites()
                GameBase.MasterGame.WriteAllText()
                GameBase.MasterGame.UpdateLightingEngine()
            case MiniGames.GameMode.TriviaGame:
                GameBase.MasterGame.DrawBackground(source=AssetLibrary.TriviaBackground)
                GameBase.MasterGame.MiniGame.PlayGame(activeGame=GameBase.MasterGame)
                EventHandler.TriviaEventHandler(activeGame=GameBase.MasterGame)

    if GameBase.MasterGame.ShowScreen:
        pygame.display.update()

    # Control the frame rate
    GameBase.MasterGame.GameClock.UpdateClock(
        clockSpeed=GameBase.MasterGame.Settings.ClockSpeed,
        frameCap=GameBase.MasterGame.Settings.CapFrames,
    )


def Setup(debugFlag=True, profileFlag=False) -> None:
    GameBase.MasterGame = GameBase.MainGame()
    pygame.event.post(CustomEvents.UpdateBackground)
    # Enables a series of functions to run automatically
    if profileFlag:
        global GAME_START_TIME
        GAME_START_TIME = time.time()
        GameBase.MasterGame.Settings.CapFrames = False
    if debugFlag:
        EventHandler.DebugSetup()


def Main(debugFlag, profileFlag, safetyFlag) -> None:
    Setup(debugFlag=debugFlag, profileFlag=profileFlag)
    while True:
        if safetyFlag:
            try:
                MainLoop()
            except Exception as e:
                print(f"{e} Occured")
        else:
            MainLoop()
        if profileFlag and time.time() - GAME_START_TIME > 30:
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debugFlag", default=True)
    parser.add_argument("-f", "--profilerFlag", default=True)
    parser.add_argument("-s", "--safetyFlag", default=False)
    args = parser.parse_args()
    Main(
        debugFlag=args.debugFlag,
        profileFlag=args.profilerFlag,
        safetyFlag=args.safetyFlag,
    )
