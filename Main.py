"""Main Body of Test"""
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "True"
import pygame
import Classes.People as pc
import Classes.Job as jc
import Classes.Game as g
import Handlers.ClickHandler as ch
import programUtils as util
from Classes.TimerBar import TimerBarClass
import Classes.Sprite as sc
import random


g.MasterGame.WorkerList.append(pc.Worker.Create())
g.MasterGame.WorkerList.append(pc.Worker.Create())
g.MasterGame.WorkerList.append(pc.Worker.Create())
g.MasterGame.CustomerList.append(pc.Customer.Create())
g.MasterGame.CustomerList.append(pc.Customer.Create())
g.MasterGame.CustomerList.append(pc.Customer.Create())



for worker in g.MasterGame.WorkerList:
    workerSprite = sc.ImageSprite((100,random.randint(1,12)*50),sc.workerPath, worker.idNum)
    g.MasterGame.SpriteGroup.add(workerSprite)

for customer in g.MasterGame.CustomerList:
    customerSprite = sc.ImageSprite((800,random.randint(1,12)*50),sc.customerPath, worker.idNum)
    g.MasterGame.SpriteGroup.add(customerSprite)

g.MasterGame.JobList.append(jc.Job.SpawnJob())
g.MasterGame.JobList[0].Assign(random.choice(g.MasterGame.CustomerList))
g.MasterGame.JobList[0].Assign(random.choice(g.MasterGame.WorkerList))

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
            ch.MouseHandler()
    g.MasterGame.SpriteGroup.update()
    for sprite in g.MasterGame.SpriteGroup:
        sprite.MvmHandler.calcNewPosition(sprite)
    # Clear the screen
    g.MasterGame.screen.fill((255, 255, 255))
    # Display the timer
    # for timer in ActiveTimerBars:
        # timer.ageTimer()
        # if(timer.completionPercentage >= 1):
            # ActiveTimerBars.remove(timer)
            # assignedTargets = jc.Job.GetAssignedFromID(JobList, timer.jobID)
            # KillList = [SpriteGroup.remove(x) for x in SpriteGroup if x.correspondingID in assignedTargets]
    
    g.MasterGame.SpriteGroup.draw(g.MasterGame.screen)
    # Update the display
    pygame.display.update()

    # Control the frame rate
    g.MasterGame.gameClock.tick(30)
