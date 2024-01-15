"""Main Body of Test"""
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "True"
import pygame
from Classes import *
from Handlers import *
import programUtils as util
import random
from multiprocessing import Process

People.Worker.CreateWorker()
People.Worker.CreateWorker()
People.Customer.CreateCustomer()

table = Sprite.BackgroundElementSprite((100, 250), Sprite.iPaths.tablePath)
table.Collision = True
Game.MasterGame.BackgroundSpriteGroup.add(table)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ClickHandler.MouseHandler()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            Game.MasterGame.Clock.ChangeClockMul(-1)
            print(Game.MasterGame.Clock.ClockMul)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
            Game.MasterGame.Clock.ChangeClockMul(1)
            print(Game.MasterGame.Clock.ClockMul)
    Game.MasterGame.screen.fill((255, 255, 255))

    for group in Game.MasterGame.SpriteGroups:
        group.update()
        for sprite in group:
            sprite.update()
    for timer in Game.MasterGame.TimerBars:
        timer.ageTimer()
        pygame.draw.rect(Game.MasterGame.screen, timer.color, timer.Rect)

    pygame.draw.lines(
        Game.MasterGame.screen, (255, 0, 0), False, Game.MasterGame.LineList
    )
    Game.MasterGame.DrawScreenClock((0, 0), ColorTools.white, ColorTools.blue)
    for group in Game.MasterGame.SpriteGroups:
        group.draw(Game.MasterGame.screen)
    # Update the display
    pygame.display.update()

    # Control the frame rate
    Game.MasterGame.Clock.UpdateClock()
