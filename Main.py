"""Main Body of Test"""

import os
import sys

# pylint: disable=wrong-import-position
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "True"
import pygame
from Classes import People, Sprite, Game, DefinedLocations, ColorTools
from Handlers import ClickHandler, SpawnHandler

DEBUGFLAG = True

if DEBUGFLAG:
    People.Worker.CreateWorker()
    People.Worker.CreateWorker()
    People.Customer.CreateCustomer()

    table = Sprite.BackgroundElementSprite((500, 250), Sprite.iPaths.TablePath)
    table.Collision = True
    Game.MasterGame.BackgroundSpriteGroup.add(table)


while True:
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

    for group in Game.MasterGame.SpriteGroups:
        group.update()
        for sprite in group:
            sprite.Update()
        group.draw(Game.MasterGame.Screen)

    for timer in Game.MasterGame.TimerBars:
        timer.UpdateAndDraw()

    SpawnHandler.SpawnHandler()
    if DEBUGFLAG:
        DefinedLocations.DebugLocations()

    Game.MasterGame.DrawScreenClock((0, 0), ColorTools.white.RGB, ColorTools.blue.RGB)
    # Update the display
    if Game.MasterGame.ShowScreen:
        pygame.display.update()

    # Control the frame rate
    Game.MasterGame.Clock.UpdateClock()
