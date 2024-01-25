import pygame
import pygame_menu
from Classes import Game
from Definitions import Prices
from Generators import CharSpawner
from dataclasses import dataclass

# TODO - Fix UnPause
def OptionsMenu(surface=Game.MasterGame.Screen) -> None:
    Game.MasterGame.GameClock.SetRunning(not Game.MasterGame.GameClock.Running)
    menu = pygame_menu.Menu(
        title="Settings",
        width=400,
        height=300,
        theme=pygame_menu.themes.THEME_BLUE,
        onclose=pygame_menu.events.CLOSE,
    )
    menu.add.toggle_switch(
        title="24 Hour Clock",
        default=Game.MasterGame.Settings.Clock24,
        state_values=("Enabled", "Disabled")
        if Game.MasterGame.Settings.Clock24
        else ("Disabled", "Enabled"),
        onchange=Game.MasterGame.Settings.ToggleClock24(),
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


def BuyNumWorkers(num) -> None:
    for i in range(num):
        CharSpawner.BuyWorker()


def ShopMenu(surface=Game.MasterGame.Screen) -> None:
    Game.MasterGame.Clock.SetRunning(not Game.MasterGame.Clock.Running)
    menu = pygame_menu.Menu(
        title="Settings",
        width=800,
        height=600,
        onclose=pygame_menu.events.CLOSE,
    )
    menu.add.range_slider(
        title="Daily Advertising Spend",
        default=0.0,
        range_values=(0, 500.0),
        increment=1.0,
        onchange=Game.MasterGame.Settings.ToggleClock24(),
    )
    menu.add.button(
        title=f"x1",
        action=lambda: (BuyNumWorkers(num=1)),
    )

    menu.add.button(title="Return", action=pygame_menu.events.CLOSE)
    menu.mainloop(surface=surface)
