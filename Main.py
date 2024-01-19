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
table.Collision = True
Game.MasterGame.BackgroundSpriteGroup.add(table)


while True:
    EventHandler.MainEventHandler()
            
    Game.MasterGame.screen.fill((255, 255, 255))
    for group in Game.MasterGame.SpriteGroups:
        group.update()
        for sprite in group:
            sprite.update()
    for timer in Game.MasterGame.TimerBars:
        timer.ageTimer()
        pygame.draw.rect(Game.MasterGame.screen, timer.color, timer.Rect)
        
    
    pygame.draw.lines(Game.MasterGame.screen, (255,0,0), False, Game.MasterGame.LineList)
    text = Game.MasterGame.font.render(f"{Game.MasterGame.Clock.dateTime}  ${Game.MasterGame.UserInventory.Money:2.2f}" , True, ColorTools.white, ColorTools.blue)
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
