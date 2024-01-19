"""Handler for Collision"""
from Classes import Game


def FindCollisionAxis(sprite, obj) -> dict[str, int]:
    obj = obj.rect
    x, y = 0, 0
    if sprite.rect.collidepoint(obj.topleft):
        x = obj.topleft[0] - sprite.rect.bottomright[0]
        y = obj.topleft[1] - sprite.rect.bottomright[1]
    elif sprite.rect.collidepoint(obj.bottomleft):
        x = obj.bottomleft[0] - sprite.rect.topright[0]
        y = obj.bottomleft[1] - sprite.rect.topright[1]
    elif sprite.rect.collidepoint(obj.topright):
        x = obj.topright[0] - sprite.rect.bottomleft[0]
        y = obj.topright[1] - sprite.rect.bottomleft[1]
    elif sprite.rect.collidepoint(obj.bottomright):
        x = obj.bottomright[0] - sprite.rect.topleft[0]
        y = obj.bottomright[1] - sprite.rect.topleft[1]

    return {"x": x, "y": y}


def CheckCollision(obj) -> None:
    for group in Game.MasterGame.SpriteGroups:
        for sprite in group:
            if (
                sprite.Collision
                and sprite.rect.colliderect(obj.rect)
                and sprite is not obj
            ):
                print(sprite)
                adjustments = FindCollisionAxis(sprite=sprite, obj=obj)
                print(adjustments)
                obj.rect.x += adjustments["x"]
                obj.rect.y += adjustments["y"]
