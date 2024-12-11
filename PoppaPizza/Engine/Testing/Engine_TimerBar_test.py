"""Test Module for Timer Bar"""

from Engine import TimerBar


def test_Timing() -> None:
    timer = TimerBar.TimerBar(duration=100, position=(0, 0), startTime=0, maxWidth=100)
    assert timer.Running == True
    assert timer.Width == 0
    timer.UpdateTimer(currentTime=5)
    assert timer.Width == 5
    assert timer.CompletionPercentage == 0.05
    timer.UpdateTimer(currentTime=50)
    assert timer.Width == 50
    assert timer.CompletionPercentage == 0.50
    timer.UpdateTimer(currentTime=-5)
    assert timer.Width == 50
    assert timer.CompletionPercentage == 0.50
    timer.UpdateTimer(currentTime=150)
    assert timer.Width == 100
    assert timer.Running == False


def test_Reset() -> None:
    timer = TimerBar.TimerBar(duration=100, position=(0, 0), startTime=0)
    timer.UpdateTimer(currentTime=110)
    assert timer.Running == False
    timer.RestartTimer(currentTime=110)
    assert timer.Running == True
    assert timer.CompletionPercentage == 0.0


def test_DynamicColor() -> None:
    timer = TimerBar.TimerBar(duration=100, position=(0, 0), startTime=0)
    timer.UpdateTimer(currentTime=50)
    assert timer.DynamicColor != timer.FillColor
    assert timer.DynamicColor != timer.TimerColor


def test_AutoReset() -> None:
    timer = TimerBar.TimerBar(duration=100, position=(0, 0), startTime=0, autoReset=True)
    timer.UpdateTimer(currentTime=90)
    assert timer.Running == True
    assert timer.StartTime == 0
    timer.UpdateTimer(currentTime=100)
    assert timer.Running == True
    timer.UpdateTimer(currentTime=110)
    assert timer.Running == True
    assert timer.StartTime == 100
