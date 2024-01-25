"""Main Body of Test"""

import os


# *OS Call used to prevent a time printout from Pygame on first import
# pylint: disable=wrong-import-position
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "True"
import pygame
from Classes import Game
from Handlers import EventHandler
from Generators import CharSpawner
from Definitions import ColorTools

Game.MasterGame = Game.Game()
# Enables a series of functions to run automatically
DEBUGFLAG = True

if DEBUGFLAG:
    EventHandler.DebugSetup()

while True:
    EventHandler.MainEventHandler()

    Game.MasterGame.DrawBackground()

    Game.MasterGame.UpdateSprites()

    # DefinedLocations.DebugLocations()
    CharSpawner.SpawnHandler()

    Game.MasterGame.DrawScreenClock(
        locationTopLeft=(0, 0),
        foreColor=ColorTools.White.RGB,
        backColor=ColorTools.Blue.RGB,
        withMoney=True,
    )

    # Update the display
    if Game.MasterGame.ShowScreen:
        pygame.display.update()
    # Control the frame rate
    Game.MasterGame.GameClock.UpdateClock()
