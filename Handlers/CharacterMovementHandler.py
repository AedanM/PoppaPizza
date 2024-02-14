from Definitions import AssetLibrary, CustomerDefs
from Engine import MovementHandler
from Handlers import QueueHandler


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
            if (
                obj.ImageType in AssetLibrary.CustomerOutfits
                and QueueHandler.NeedsToQueue(movingSprite=obj)
            ):
                obj.DataObject.CurrentState = CustomerDefs.CustomerStates.Queuing
            else:
                super().CalcNewPosition(
                    obj=obj, gameSpeed=activeGame.GameClock.ClockMul
                )
