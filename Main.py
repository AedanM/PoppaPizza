"""Main Body of Game"""

import os

# *OS Call used to prevent a time printout from Pygame on first import
# pylint: disable=wrong-import-position
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "True"
import pygame

from Classes import Game
from Definitions import CustomEvents
from Handlers import EventHandler


def Main() -> None:
    """Main Loop of Game"""
    Game.MasterGame = Game.Game()
    pygame.event.post(CustomEvents.UpdateBackground)
    # Enables a series of functions to run automatically
    debugFlag = True

    if debugFlag:
        EventHandler.DebugSetup()
    while True:
        if Game.MasterGame.Running:
            EventHandler.MainEventHandler()

            Game.MasterGame.DrawBackground()
            Game.MasterGame.UpdateSprites()
            # DefinedLocations.DebugLocations()
            EventHandler.RandomSpawnHandler()
            Game.MasterGame.WriteAllText()
            # Update the display
        if Game.MasterGame.ShowScreen:
            pygame.display.update()
        # Control the frame rate
        Game.MasterGame.GameClock.UpdateClock()


if __name__ == "__main__":
    Main()
