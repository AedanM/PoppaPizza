"""Main Body of Test"""

import os
import sys


# *OS Call used to prevent a time printout from Pygame on first import
# pylint: disable=wrong-import-position
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "True"
import pygame
from Classes import People, Game, DefinedLocations, ColorTools
from Handlers import EventHandler
from Generators import CharSpawner, BackgroundPopulator

Game.MasterGame = Game.Game()
# Enables a series of functions to run automatically
DEBUGFLAG = True

if DEBUGFLAG:
    CharSpawner.WorkerSpawner(force=True)
    CharSpawner.WorkerSpawner(force=True)
    CharSpawner.CustomerSpawner(force=True)
    BackgroundPopulator.AddTables()

while True:
    EventHandler.MainEventHandler()

    Game.MasterGame.DrawBackground()

    Game.MasterGame.UpdateSprites()

    Game.MasterGame.UpdateTimers()

    CharSpawner.SpawnHandler()

    if DEBUGFLAG:
        DefinedLocations.DebugLocations()

    Game.MasterGame.DrawScreenClock(
        locationTopLeft=(0, 0),
        foreColor=ColorTools.white.RGB,
        backColor=ColorTools.blue.RGB,
    )

    # Update the display
    if Game.MasterGame.ShowScreen:
        pygame.display.update()

    # Control the frame rate
    Game.MasterGame.Clock.UpdateClock()
