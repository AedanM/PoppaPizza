"""Main Body of Test"""

import os
import sys
import random
from multiprocessing import Process

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "True"
import pygame
from Classes import *
from Handlers import *

People.Worker.CreateWorker()
People.Worker.CreateWorker()
People.Customer.CreateCustomer()

table = Sprite.BackgroundElementSprite((100, 250), Sprite.iPaths.TablePath)
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

    Game.MasterGame.Screen.fill((255, 255, 255))

    for group in Game.MasterGame.SpriteGroups:
        group.update()
        for sprite in group:
            sprite.Update()

    for timer in Game.MasterGame.TimerBars:
        timer.AgeTimer()
        pygame.draw.rect(Game.MasterGame.Screen, timer.Color, timer.Rect)

    SpawnHandler.SpawnHandler()

    pygame.draw.lines(
        Game.MasterGame.Screen, (255, 0, 0), False, Game.MasterGame.LineList
    )
    Game.MasterGame.DrawScreenClock((0, 0), ColorTools.white, ColorTools.blue)

    for group in Game.MasterGame.SpriteGroups:
        group.draw(Game.MasterGame.Screen)
    # Update the display
    if Game.MasterGame.ShowScreen:
        pygame.display.update()

    # Control the frame rate
    Game.MasterGame.Clock.UpdateClock()
