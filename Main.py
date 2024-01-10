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

table = Sprite.BackgroundElementSprite((250, 250), Sprite.iPaths.tablePath)
Game.MasterGame.BackgroundSpriteGroup.add(table)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ClickHandler.MouseHandler()

    for group in Game.MasterGame.SpriteGroups:
        group.update()
        for sprite in group:
            sprite.update()
    # Clear the screen
    Game.MasterGame.screen.fill((255, 255, 255))
    # Display the timer
    # for timer in ActiveTimerBars:
    # timer.ageTimer()
    # if(timer.completionPercentage >= 1):
    # ActiveTimerBars.remove(timer)
    # assignedTargets = jc.Job.GetAssignedFromID(JobList, timer.jobID)
    # KillList = [SpriteGroup.remove(x) for x in SpriteGroup if x.correspondingID in assignedTargets]

    for group in Game.MasterGame.SpriteGroups:
        group.draw(Game.MasterGame.screen)
    # Update the display
    pygame.display.update()

    # Control the frame rate
    Game.MasterGame.gameClock.tick(30)
