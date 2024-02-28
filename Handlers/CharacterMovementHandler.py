from AtomicbritEngine.Engine import MovementHandler, Utils
from Definitions import AssetLibrary
from Definitions.CustomerDefs import CustomerStates, QueueStates

QUEUEDISTANCE = 75


class CharacterMovementHandler(MovementHandler.MovementHandler):
    """Character Movement Handler

        Handles all Motion Features for a Sprite

    Returns-
        CharacterMovementHandler:
    """

    def CalcNewPosition(self, obj, activeGame) -> None:
        """Logic for Moving Characters and Queuing

        Args-
            obj (Sprite): Moving Sprite
        """
        if activeGame.GameClock.Running:
            if obj.ImageType in AssetLibrary.CustomerOutfits and NeedsToQueue(
                movingSprite=obj, activeGame=activeGame
            ):
                obj.DataObject.CurrentState = CustomerStates.Queuing
            else:
                super().CalcNewPosition(obj=obj, gameSpeed=activeGame.GameClock.ClockMul)


def NeedsToQueue(movingSprite, activeGame) -> bool:
    """Checks if the Customer needs to Queue

    Args-
        movingSprite (Sprite): Customer

    Returns-
        bool: Does the customer have to queue
    """
    dataObject = movingSprite.DataObject
    match dataObject.CurrentState:
        case CustomerStates.Queuing:
            if FirstInLine(movingSprite=movingSprite, activeGame=activeGame):
                dataObject.CurrentState = CustomerStates.FirstInLine
                return False

            dataObject.CurrentState = CustomerStates.WalkingIn
            return NeedsToQueue(movingSprite=movingSprite, activeGame=activeGame)

        case CustomerStates.WalkingIn:
            for sprite in activeGame.CharSpriteGroup:
                if (
                    sprite is not movingSprite
                    and sprite.ImageType in AssetLibrary.CustomerOutfits
                    and sprite.DataObject.CurrentState in QueueStates
                    and Utils.PositionInTolerance(
                        pos1=sprite.rect.center,
                        pos2=movingSprite.rect.center,
                        tolerance=QUEUEDISTANCE,
                    )
                ):
                    return True
    return False


def FirstInLine(movingSprite, activeGame) -> bool:
    """Checks if the customer is first in Queue

    Args-
        movingSprite (Sprite): Customer Sprite

    Returns-
        bool: Is the Customer the first in the line
    """
    for sprite in activeGame.CharSpriteGroup:
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
