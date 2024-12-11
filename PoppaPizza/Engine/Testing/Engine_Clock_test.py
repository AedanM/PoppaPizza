"""Test Module for Clock"""

import time

import pygame
from Engine import Clock, Utils
from Engine.Testing.TestClass import TestClass


def RunClockForRealTime(clock, lenInSeconds, clockMul=1.0) -> tuple[int, int]:
    prevTime = clock.Minute
    startTime = time.time()
    while time.time() - lenInSeconds < startTime:
        clock.UpdateClock(clockSpeed=clockMul, frameCap=60)
    return prevTime, clock.Minute


def test_PauseClock() -> None:
    # pylint: disable=E1101
    clock = Clock.Clock(pygame.Clock()) # type: ignore

    clock.SetRunning(False)
    start, end = RunClockForRealTime(clock=clock, lenInSeconds=1)
    assert start == end

    clock.SetRunning(True)
    start, end = RunClockForRealTime(clock=clock, lenInSeconds=1)
    assert start < end


def test_ClockSpeeds() -> None:
    # pylint: disable=E1101
    clock = Clock.Clock(pygame.Clock()) # type: ignore
    tolerance = 3
    testObjects = [
        TestClass(ParamList=[0.5], Result=8),
        TestClass(ParamList=[0.25], Result=4),
        TestClass(ParamList=[0.125], Result=2),
        TestClass(ParamList=[1], Result=16),
        TestClass(ParamList=[2], Result=32),
        TestClass(ParamList=[4], Result=64),
    ]
    for test in testObjects:
        start, end = RunClockForRealTime(clock=clock, lenInSeconds=1, clockMul=test.ParamList[0])
        try:
            assert Utils.InTolerance(
                num1=(end - start), num2=test.Result, tolerance=tolerance
            )
        except AssertionError:
            print(test, end - start)
            assert False
