import math
import sys

if __name__ == "__main__":
    sys.path.insert(0, "../Classes")
    sys.path.insert(0, "..")
    import Game as Game
else:
    import Classes.Game as Game
import Classes.utils as utils
import pygame
import random


def removeDupes(l):
    for idx, i in enumerate(l):
        if l.count(i) > 1:
            del l[idx]
    return l


def GenLandmarksBetween(point1, point2, speed):
    pointList = [point1, point2]
    ysteps = abs((point2[1] - point1[1]) / speed)
    xsteps = abs((point2[0] - point1[0]) / speed)
    if xsteps < 1 and ysteps < 1:
        return pointList
    elif xsteps != ysteps and xsteps != 0 and ysteps != 0:
        reachToNew = abs(point2[1] - point1[1])
        signX = utils.sign(point2[0] - point1[0])
        # print(point2, point1, reachToNew , signX)
        newX = point1[0] + (reachToNew * signX)
        newX = point2[1] if (newX * signX) > (point2[0] * signX) else point2[0]
        newPoint = (point1[0] + (reachToNew * signX), point2[1])
        pointList = GenLandmarksBetween(point1, newPoint, speed) + GenLandmarksBetween(
            newPoint, point2, speed
        )
        return removeDupes(pointList)
    else:
        return pointList
    return removeDupes(pointList)


def RectInLine(rect, point1, point2):
    pointRect = pygame.Rect(point1[0], point1[1], 100, 100)
    pointRect.center = ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)
    return pygame.Rect.colliderect(pointRect, rect)


def CheckCollision(pointPath, rectList):
    print(pointPath)
    for i in range(len(pointPath)):
        if i != 0:
            p1 = pointPath[i - 1]
            p2 = pointPath[i]
            for rect in rectList:
                if RectInLine(rect, p1, p2):
                    print("hit")
                    pointPath.insert(i, (1, 1))
    return removeDupes(pointPath)


def CleanTweenPoints(pointList):
    prevDirect = (0, 0)
    direct = (0, 0)
    tweenedList = [pointList[0]]
    for index, point in enumerate(pointList):
        if index != 0:
            prevPoint = pointList[index - 1]
            direct = ((point[0] - prevPoint[0]), (point[1] - prevPoint[1]))
        if direct != prevDirect:
            tweenedList.append(point)
        prevDirect = direct
    tweenedList.append(pointList[-1])
    return tweenedList


def CreatePath(startPoint, endPoint, speed, backgroundObs):
    print()
    tightPath = [
        startPoint,
        endPoint,
    ]  # GenLandmarksBetween(startPoint, endPoint, speed)
    finalPath = CheckCollision(tightPath, backgroundObs)
    print(finalPath)
    return finalPath


class Ctest:
    def __init__(self, p1: tuple, p2: tuple, speed, result: list):
        self.p1 = p1
        self.p2 = p2
        self.speed = speed
        self.result = result


def GenLandmarksBetweenUnitTest():
    tests = [
        # 0-7
        Ctest(p1=(600, 400), p2=(800, 600), speed=100, result=[(600, 400), (800, 600)]),
        Ctest(p1=(600, 400), p2=(400, 200), speed=100, result=[(600, 400), (400, 200)]),
        Ctest(p1=(600, 400), p2=(600, 200), speed=100, result=[(600, 400), (600, 200)]),
        Ctest(p1=(600, 400), p2=(600, 600), speed=100, result=[(600, 400), (600, 600)]),
        Ctest(p1=(600, 400), p2=(400, 400), speed=100, result=[(600, 400), (400, 400)]),
        Ctest(p1=(600, 400), p2=(800, 400), speed=100, result=[(600, 400), (800, 400)]),
        Ctest(p1=(600, 400), p2=(800, 200), speed=100, result=[(600, 400), (800, 200)]),
        Ctest(p1=(600, 400), p2=(400, 600), speed=100, result=[(600, 400), (400, 600)]),
        # 8
        Ctest(
            p1=(600, 400),
            p2=(250, 575),
            speed=100,
            result=[(600, 400), (425, 575), (250, 575)],
        ),
        Ctest(
            p1=(600, 400),
            p2=(250, 150),
            speed=100,
            result=[(600, 400), (350, 150), (250, 150)],
        ),
        Ctest(
            p1=(600, 400),
            p2=(950, 575),
            speed=100,
            result=[(600, 400), (775, 575), (950, 575)],
        ),
        Ctest(
            p1=(600, 400),
            p2=(950, 150),
            speed=100,
            result=[(600, 400), (850, 150), (950, 150)],
        ),
    ]
    for test in tests:
        points = GenLandmarksBetween(test.p1, test.p2, test.speed)
        pygame.draw.circle(Game.MasterGame.screen, (0, 255, 0), (600, 400), 25)
        col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.lines(
            Game.MasterGame.screen,
            col,
            False,
            points,
        )
        text = Game.MasterGame.font.render(
            str(tests.index(test)), True, col, (255, 255, 255)
        )
        textRect = text.get_rect()
        textRect.center = (300, 200)
        Game.MasterGame.screen.blit(text, textRect)
        pygame.display.update()
        assert points == test.result, str(points) + " Failed"
        print(str(tests.index(test)) + " Passed")
        x = input()


if __name__ == "__main__":
    while True:
        Game.MasterGame.screen.fill((255, 255, 255))
        GenLandmarksBetweenUnitTest()
        pygame.display.update()
