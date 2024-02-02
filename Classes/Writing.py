"""Functions for Text Generation"""

from Definitions import ColorTools
from Utilities import Utils


def CreateTextBox(
    locationTopLeft, text, foreColor, font, screen, backColor=None
) -> None:
    text = (
        font.render(text, False, foreColor.RGB)
        if not backColor
        else font.render(text, False, foreColor.RGB, backColor.RGB)
    )
    textrect = text.get_rect()
    textrect.x = locationTopLeft[0]
    textrect.y = locationTopLeft[1]
    screen.blit(source=text, dest=textrect)


def WriteDateLabel(activeGame) -> None:
    clockText = (
        f"{activeGame.GameClock.DateTime} ${activeGame.UserInventory.Money:0.2f}"
    )

    CreateTextBox(
        locationTopLeft=(0, 0),
        text=clockText,
        foreColor=ColorTools.White,
        backColor=ColorTools.Blue,
        font=activeGame.Font,
        screen=activeGame.Screen,
    )


def WriteButtonLabel(activeGame) -> None:
    for button in activeGame.ButtonList:
        CreateTextBox(
            locationTopLeft=Utils.OffsetTuple(
                inputTuple=button.position, offset=(-45, -12)
            ),
            text=button.text,
            foreColor=ColorTools.Black,
            font=activeGame.Font,
            screen=activeGame.Screen,
        )
