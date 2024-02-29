"""Main Body of Game"""

import argparse
import os

# *OS Call used to prevent a time printout from Pygame on first import
# pylint: disable=wrong-import-position
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "True"
import time

import pygame

from Classes import GameBase, MiniGames
from Definitions import AssetLibrary, CustomEvents
from Handlers import EventHandler

GAME_START_TIME = 0


def MainLoop(CurrentGame: GameBase.MainGame) -> None:
    """Main Loop of Game"""
    if CurrentGame.Running:
        match CurrentGame.Mode:
            case MiniGames.GameMode.Base:
                EventHandler.MainEventHandler(activeGame=CurrentGame)
                CurrentGame.DrawBackground(source=AssetLibrary.Background)
                CurrentGame.UpdateSprites()
                CurrentGame.WriteAllText()
                CurrentGame.UpdateLightingEngine()
            case MiniGames.GameMode.TriviaGame:
                CurrentGame.DrawBackground(source=AssetLibrary.TriviaBackground)
                CurrentGame.MiniGame.PlayGame(activeGame=CurrentGame)
                EventHandler.TriviaEventHandler(activeGame=CurrentGame)

    if CurrentGame.ShowScreen:
        pygame.display.update()
    # Control the frame rate
    CurrentGame.GameClock.UpdateClock(
        clockSpeed=CurrentGame.Settings.ClockSpeed,
        frameCap=CurrentGame.Settings.CapFrames,
    )


def Setup(debugFlag: bool = True, profileFlag: bool = False) -> GameBase.MainGame:
    CurrentGame = GameBase.MainGame()
    pygame.event.post(CustomEvents.UpdateBackground)
    # Enables a series of functions to run automatically
    if profileFlag:
        global GAME_START_TIME
        GAME_START_TIME = time.time()
        CurrentGame.Settings.CapFrames = False
    if debugFlag:
        EventHandler.DebugSetup(activeGame=CurrentGame)
    return CurrentGame


def Main(debugFlag: bool, profileFlag: bool, safetyFlag: bool) -> None:
    MainGame = Setup(debugFlag=debugFlag, profileFlag=profileFlag)
    while True:
        if safetyFlag:
            try:
                MainLoop(CurrentGame=MainGame)
            except Exception as e:
                print(f"{e} Occured")
        else:
            MainLoop(CurrentGame=MainGame)
        if profileFlag and time.time() - GAME_START_TIME > 30:
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debugFlag", default="True")
    parser.add_argument("-p", "--profilerFlag", default="False")
    parser.add_argument("-s", "--safetyFlag", default="False")
    args = parser.parse_args()
    Main(
        debugFlag=args.debugFlag.capitalize() == "True",
        profileFlag=args.profilerFlag.capitalize() == "True",
        safetyFlag=args.safetyFlag.capitalize() == "True",
    )
