"""Main Body of Test"""
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "True"
import pygame
from Classes import *
from Handlers import *
import programUtils as util
import random


People.Worker.CreateWorker()
People.Customer.CreateCustomer()

table = Sprite.BackgroundElementSprite((100, 250), Sprite.iPaths.tablePath)
table.Collision = False
Game.MasterGame.BackgroundSpriteGroup.add(table)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ClickHandler.MouseHandler()
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_t):
            Game.MasterGame.Clock.ChangeClockMul(-1)
            print(Game.MasterGame.Clock.ClockMul)
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_y):
            Game.MasterGame.Clock.ChangeClockMul(1)
            print(Game.MasterGame.Clock.ClockMul)

    for group in Game.MasterGame.SpriteGroups:
        group.update()
        for sprite in group:
            sprite.update()
    Game.MasterGame.screen.fill((255, 255, 255))
    
    text = Game.MasterGame.font.render(str(Game.MasterGame.Clock.dateTime), True, ColorTools.white, ColorTools.blue)
    textRect = text.get_rect()
    textRect.x = 0
    textRect.y = 0
    Game.MasterGame.screen.blit(text, textRect)
    for group in Game.MasterGame.SpriteGroups:
        group.draw(Game.MasterGame.screen)
    # Update the display
    pygame.display.update()

    # Control the frame rate
    Game.MasterGame.Clock.UpdateClock()
