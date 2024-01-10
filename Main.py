"""Main Body of Test"""
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "True"
import pygame
from Classes import *
from Handlers import *
import programUtils as util
import random


Game.MasterGame.WorkerList.append(People.Worker.Create())
# g.MasterGame.WorkerList.append(pc.Worker.Create())
# g.MasterGame.WorkerList.append(pc.Worker.Create())
People.Customer.CreateCustomer()
# g.MasterGame.CustomerList.append(pc.Customer.Create())
# g.MasterGame.CustomerList.append(pc.Customer.Create())

for worker in Game.MasterGame.WorkerList:
    workerSprite = Sprite.CharImageSprite(
        (100, random.randint(1, 12) * 50), Sprite.iPaths.workerPath, worker.idNum
    )
    Game.MasterGame.CharSpriteGroup.add(workerSprite)





table = Sprite.BackgroundElementSprite((250,250), Sprite.iPaths.tablePath)
Game.MasterGame.BackgroundSpriteGroup.add(table)


# for c in CustomerList:
# ActiveTimerBars.append(
# TimerBarClass(
# duration=c.desiredJob.Length, displayScreen=screen, position=(50, 100), jobID=c.desiredJob.JobId
# )
# )


# for timerBar in ActiveTimerBars:
# timerBar.startTimer()
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
            if(sprite.Moveable):
                sprite.MvmHandler.calcNewPosition(sprite)
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
