"""Test Module for Movement Handler"""

from Engine import MovementHandler, SpriteObjects


def test_ListedMotion() -> None:
    rect1 = SpriteObjects.RectangleObject(position=(0, 0))
    mvmHandler = MovementHandler.MovementHandler()

    path = [rect1.rect.center, (1000, 1000), (0, 0)]
    mvmHandler.StartNewListedMotion(pointList=path, speed=100)
    assert mvmHandler.DstSet
    mvmHandler.CalcNewPosition(obj=rect1, gameSpeed=1)
    mvmHandler.CalcNewPosition(obj=rect1, gameSpeed=1)
    assert mvmHandler.Dest == (1000, 1000)
    mvmHandler.CalcNewPosition(obj=rect1, gameSpeed=1)
    mvmHandler.CalcNewPosition(obj=rect1, gameSpeed=1)
    assert rect1.rect.center == (300, 300)
    steps = 0
    while mvmHandler.InMotion:
        assert steps < 10 + 7
        mvmHandler.CalcNewPosition(obj=rect1, gameSpeed=1)
        steps += 1


def test_Reset() -> None:
    rect1 = SpriteObjects.RectangleObject(position=(1, 1))
    mvmHandler = MovementHandler.MovementHandler()
    path = [rect1.rect.center, (1000, 1000), (0, 0)]
    mvmHandler.StartNewListedMotion(pointList=path, speed=100)
    assert mvmHandler.DstSet
    mvmHandler.CalcNewPosition(obj=rect1, gameSpeed=1)
    mvmHandler.CalcNewPosition(obj=rect1, gameSpeed=1)
    mvmHandler.Reset()
    assert mvmHandler.DstSet == False
    assert mvmHandler.InMotion == False
