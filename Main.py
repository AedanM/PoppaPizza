"""Main Body of Game"""

import argparse
import os

# *OS Call used to prevent a time printout from Pygame on first import
# pylint: disable=wrong-import-position
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "True"
import threading
import time

import pygame

from Classes import Game
from Definitions import AssetLibrary, CustomEvents
from Handlers import EventHandler


def Main() -> None:
    """Main Loop of Game"""
    debugFlag = True
    profileFlag = False
    Game.MasterGame = Game.Game()
    pygame.event.post(CustomEvents.UpdateBackground)
    # Enables a series of functions to run automatically
    if profileFlag:
        startTime = time.time()
    if debugFlag:
        EventHandler.DebugSetup()
    while True:
        if Game.MasterGame.Running:
            try:
                EventHandler.MainEventHandler()
                Game.MasterGame.DrawBackground()
                Game.MasterGame.UpdateSprites()
                Game.MasterGame.WriteAllText()
                Game.MasterGame.UpdateLightingEngine()

            except Exception as e:
                print(f"{e} Occured")
        if Game.MasterGame.ShowScreen:
            pygame.display.update()

        # Control the frame rate
        Game.MasterGame.GameClock.UpdateClock()
        if profileFlag and (time.time() - startTime > 15):
            break


if __name__ == "__main__":
    Main()
