"""Main Body of Test"""

import os
import sys


# *OS Call used to prevent a time printout from Pygame on first import
# pylint: disable=wrong-import-position
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "True"
import pygame
from Classes import People, Sprite, Game, DefinedLocations, ColorTools
from Handlers import ClickHandler
from Generators import CharSpawner, BackgroundPopulator

# Enables a series of functions to run automatically
DEBUGFLAG = True

if DEBUGFLAG:
    People.Worker.CreateWorker()
    People.Worker.CreateWorker()
    People.Customer.CreateCustomer()
    BackgroundPopulator.AddTables()

while True:
    # TODO: Move to EventHandler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ClickHandler.MouseHandler()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            Game.MasterGame.Clock.ChangeClockMul(-1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
            Game.MasterGame.Clock.ChangeClockMul(1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            People.Worker.CreateWorker()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            People.Customer.CreateCustomer()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            Game.MasterGame.ShowScreen = not Game.MasterGame.ShowScreen

    Game.MasterGame.DrawBackground()

    Game.MasterGame.UpdateSprites()

    Game.MasterGame.UpdateTimers()

    CharSpawner.SpawnHandler()

    if DEBUGFLAG:
        DefinedLocations.DebugLocations()

    Game.MasterGame.DrawScreenClock((0, 0), ColorTools.white.RGB, ColorTools.blue.RGB)

    # Update the display
    if Game.MasterGame.ShowScreen:
        pygame.display.update()

    # Control the frame rate
    Game.MasterGame.Clock.UpdateClock()
