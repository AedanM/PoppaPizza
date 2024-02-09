"""Main Body of Game"""

import os

# *OS Call used to prevent a time printout from Pygame on first import
# pylint: disable=wrong-import-position
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "True"
import time

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
    timingDict = {
        "Event": 0,
        "Lighting": 0,
        "Background": 0,
        "Sprite": 0,
        "Writing": 0,
        "Update": 0,
        "Clock": 0,
        "NumFrames": 0,
    }
    while True:
        timeStart = time.time()
        if Game.MasterGame.Running:
            try:
                EventHandler.MainEventHandler()
                eventTime = time.time()
                timingDict["Event"] += eventTime - timeStart

                Game.MasterGame.DrawBackground()
                backgroundTime = time.time()
                timingDict["Background"] += backgroundTime - eventTime

                Game.MasterGame.UpdateSprites()
                spriteTime = time.time()
                timingDict["Sprite"] += spriteTime - backgroundTime

                Game.MasterGame.WriteAllText()
                writeTime = time.time()
                timingDict["Writing"] += writeTime - spriteTime

                Game.MasterGame.UpdateLightingEngine()
                lightTime = time.time()
                timingDict["Lighting"] += lightTime - writeTime

            except Exception as e:
                print(f"{e} Occured")
        if Game.MasterGame.ShowScreen:
            pygame.display.update()
            updateTime = time.time()
            timingDict["Update"] += updateTime - lightTime

        # Control the frame rate
        Game.MasterGame.GameClock.UpdateClock()
        clockTime = time.time()
        timingDict["Clock"] += clockTime - updateTime
        timingDict["NumFrames"] += 1
        if timingDict["NumFrames"] > 1000:
            pass


if __name__ == "__main__":
    Main()
