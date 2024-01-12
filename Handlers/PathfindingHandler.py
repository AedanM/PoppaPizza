import math
import sys
sys.path.insert(0,'../Classes')
import Game as Game
import pygame

def removeDupes(l):
    for idx,i in enumerate(l):
        if(l.count(i) > 1):
            del l[idx]
    return l

def GenLandmarksBetween(point1, point2, speed):
    pointList = [point1,point2]
    print(pointList, speed)
    ysteps = (point2[1] - point1[1]) / speed
    xsteps = (point2[0] - point1[0]) / speed
    if(xsteps != ysteps and xsteps != 0 and ysteps != 0):
        print(xsteps, ysteps)
        newPoint = (point2[0],point2[0])
        pointList = GenLandmarksBetween(point1, newPoint, speed) + GenLandmarksBetween(newPoint, point2, speed)
    else:
        return pointList
    return (removeDupes(pointList))

def RectInLine(rect,point1, point2):
    pointRect = pygame.Rect(
        point1[0],
        point1[1],
        abs(point1[0]-point2[0]),
        abs(point1[1]-point2[1])
    )
    return pygame.Rect.colliderect(pointRect,rect)

    
    
def CheckCollision(pointPath, rectList):
    print(pointPath)
    for i in range(len(pointPath)):
        if(i != 0):
            p1 = pointPath[i-1]
            p2 = pointPath[i]
            for rect in rectList:
                if(RectInLine(rect, p1, p2)):
                    pointPath.insert(i-1,(1,1))
    return(pointPath)
def CleanTweenPoints(pointList):
    prevDirect = (0,0)
    direct = (0,0)
    tweenedList = [pointList[0]]
    for index,point in enumerate(pointList):
        if(index != 0):
            prevPoint = pointList[index-1]
            direct = (
                (point[0] - prevPoint[0]),
                (point[1] - prevPoint[1])
            )
        if(direct != prevDirect):
            tweenedList.append(point)
        prevDirect = direct
    tweenedList.append(pointList[-1])
    return tweenedList
  
  
def CreatePath(startPoint, endPoint, speed, background):
    tightPath = GenLandmarksBetween(startPoint, endPoint, speed)
    finalPath = CheckCollision(tightPath, backgroundObs)
    return finalPath

class Ctest:
    def __init__(p1: tuple, p2: tuple, speed, result:list):
        self.p1 = p1
        self.p2 = p2
        self.speed = speed
        self.result = result
    
def GenLandmarksBetweenUnitTest():
    tests = [
       Ctest(p1=(0,0), p2=(10,10), speed=1, result=[(0,0),(10,10)])
    
    ]
    for test in tests:
        assert(GenLandmarksBetween(test.p1,test.p2, test.p3) == tests.result), GenLandmarksBetween(test.p1,test.p2, test.p3)

    

if __name__ == '__main__':
    GenLandmarksBetweenUnitTest()
    p1 = (525,183)
    p2 = (349,538)
    while True:
        Game.MasterGame.screen.fill((255, 255, 255))
        pygame.draw.lines(Game.MasterGame.screen, (255, 136, 0), False, GenLandmarksBetween(p1,p2, 1))
        pygame.display.update()
