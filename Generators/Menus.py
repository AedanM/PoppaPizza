"""Generator Functions for Menus"""

import pygame_menu

from Classes import Game
from Generators import CharSpawner


def OpenMenu() -> None:
    Game.MasterGame.GameClock.SetRunning(state=False)


def CloseMenu() -> None:
    Game.MasterGame.GameClock.SetRunning(state=True)


def BuyNumWorkers(num) -> None:
    for _ in range(num):
        CharSpawner.BuyWorker()


def DayTransistion(activeGame=Game.MasterGame) -> None:
    OpenMenu()
    menu = pygame_menu.Menu(
        title="End of Day",
        width=800,
        height=600,
        theme=pygame_menu.themes.THEME_GREEN,
        onclose=CloseMenu,
    )
    menu.add.label(title=f"Day {Game.MasterGame.GameClock.Day}", label_id="Title")
    menu.get_widget(widget_id="Title").scale(width=2, height=2, smooth=True)
    menu.add.label(
        title=f"Customers Served: {Game.MasterGame.UserInventory.Statistics.GetServedCustomers()} / {Game.MasterGame.UserInventory.Statistics.GetTotalCustomers()}"
    )
    menu.add.label(
        title=f"Money Earned: {Game.MasterGame.UserInventory.Statistics.GetEarnings():.2f}"
    )
    menu.add.label(
        title=f"Money Spent: {Game.MasterGame.UserInventory.Statistics.GetSpend():.2f}"
    )
    menu.add.button(title="Continue to Next Day", action=pygame_menu.events.CLOSE)
    menu.mainloop(surface=activeGame.Screen, wait_for_event=True)


def OptionsMenu(surface=Game.MasterGame.Screen) -> None:
    OpenMenu()
    menu = pygame_menu.Menu(
        title="Settings",
        width=400,
        height=300,
        theme=pygame_menu.themes.THEME_BLUE,
        onclose=CloseMenu,
    )
    menu.add.toggle_switch(
        toggleswitch_id="24Toggle",
        title="24 Hour Clock",
        default=Game.MasterGame.Settings.Clock24,
        state_text=("Off", "On"),
        state_values=(False, True),
        onchange=lambda x: Game.MasterGame.Settings.SetClock24(value=x),
    )
    menu.add.range_slider(
        title="Speed",
        default=0,
        range_values=list(
            range(
                Game.MasterGame.Settings.ClockPowRange[0],
                Game.MasterGame.Settings.ClockPowRange[1] + 1,
            )
        ),
        value_format=lambda x: f"{pow(base=2, exp=x)}x",
        range_text_value_enabled=False,
        onchange=lambda x: (Game.MasterGame.Settings.SetClockMul(value=x)),
    )
    menu.add.button(title="Return", action=pygame_menu.events.CLOSE)
    menu.mainloop(surface=surface, wait_for_event=True)


def ShopMenu(surface=Game.MasterGame.Screen) -> None:
    OpenMenu()
    menu = pygame_menu.Menu(
        title="Shop",
        width=800,
        height=600,
        theme=pygame_menu.themes.THEME_BLUE,
        onclose=CloseMenu,
    )
    menu.add.range_slider(
        title="Daily Advertising Spend",
        default=0.0,
        range_values=(0, 500.0),
        increment=1.0,
    )
    menu.add.button(
        title="x1",
        action=lambda: (BuyNumWorkers(num=1)),
    )
    menu.add.button(title="Return", action=pygame_menu.events.CLOSE)
    menu.mainloop(surface=surface, wait_for_event=True)


def GameOverMenu(
    surface=Game.MasterGame.Screen, reason="\n You ran out of Money"
) -> None:
    OpenMenu()
    menu = pygame_menu.Menu(
        title="Game Over",
        width=Game.MasterGame.Screen.get_width(),
        height=Game.MasterGame.Screen.get_height(),
        onclose=pygame_menu.events.EXIT,
        theme=pygame_menu.themes.THEME_DARK,
    )
    menu.add.label(title=f"Game Over {reason}\n\n", font_size=60, font_shadow=True)
    menu.add.button(title="Close Game", action=pygame_menu.events.EXIT)
    menu.mainloop(surface=surface)
