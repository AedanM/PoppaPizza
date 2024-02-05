"""Handler for Queueing Actions"""

from Classes import Game
from Definitions import AssetLibrary, CustomerDefs
from Utilities import Utils

QUEUEDISTANCE = 75


def NeedsToQueue(movingSprite) -> bool:
    dataObject = movingSprite.DataObject
    match dataObject.CurrentState:
        case CustomerDefs.CustomerStates.Queuing:
            if FirstInLine(movingSprite=movingSprite):
                dataObject.CurrentState = CustomerDefs.CustomerStates.FirstInLine
                return False

            dataObject.CurrentState = CustomerDefs.CustomerStates.WalkingIn
            return NeedsToQueue(movingSprite=movingSprite)

        case CustomerDefs.CustomerStates.WalkingIn:
            for sprite in Game.MasterGame.CharSpriteGroup:
                if (
                    sprite is not movingSprite
                    and sprite.ImageType in AssetLibrary.CustomerOutfits
                    and sprite.DataObject.CurrentState in CustomerDefs.QueueStates
                    and Utils.PositionInTolerance(
                        pos1=sprite.rect.center,
                        pos2=movingSprite.rect.center,
                        tolerance=QUEUEDISTANCE,
                    )
                ):
                    return True
        # pylint: disable=unused-variable
        case other:
            return False


def FirstInLine(movingSprite) -> bool:
    for sprite in Game.MasterGame.CharSpriteGroup:
        if (
            sprite is not movingSprite
            and sprite.rect.centerx == movingSprite.rect.centerx
            and sprite.rect.centery < movingSprite.rect.centery
            and Utils.PositionInTolerance(
                pos1=sprite.rect.center,
                pos2=movingSprite.rect.center,
                tolerance=QUEUEDISTANCE,
            )
        ):
            return False
    return True
