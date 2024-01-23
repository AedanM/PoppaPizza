"""Utilites"""
import math
import socket
import random
import string
from typing import Any


# TODO- Worth a unit test?
def CheckInternet(host="8.8.8.8", port=53, timeout=30) -> bool:
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    except OSError:
        return False
    return True


def InRandomVariance(num, percentVariance) -> float:
    percentVariance = checkDecimalPercent(percentVariance)
    varyAmount = random.randint(a=-100, b=100) * percentVariance * 0.01 * num
    return num + varyAmount


def checkDecimalPercent(val) -> float | tuple:
    if type(val) == tuple:
        holdList = []
        percentMod = True if (abs(val[0]) < 1) else False
        for i in val:
            holdList.append(float(i) if percentMod else float(i) / 100)
        return tuple(holdList)
    else:
        return float(val) if abs(val) <= 1 else float(val) / 100


def PositionRandomVariance(
    position, percentVarianceTuple, screenSize
) -> tuple[int, int]:
    percentVarianceTuple = checkDecimalPercent(val=percentVarianceTuple)
    varyAmountX = math.ceil(
        (random.randint(-100, 100) * 0.01 * percentVarianceTuple[0] * screenSize[0])
        + position[0]
    )
    varyAmountY = math.ceil(
        (random.randint(-100, 100) * 0.01 * percentVarianceTuple[1] * screenSize[1])
        + position[1]
    )
    out = (
        Bind(val=varyAmountX, inRange=(0, screenSize[0])),
        Bind(val=varyAmountY, inRange=(0, screenSize[1])),
    )
    return out


def InTolerance(num1, num2, tolerance) -> bool:
    return abs(num1 - num2) <= abs(tolerance)


def InPercentTolerance(num1, num2, tolerance) -> bool:
    tolerance = checkDecimalPercent(val=tolerance)
    if num1 == 0:
        return False
    seperation = abs((num1 - num2) / num1)
    return seperation <= abs(tolerance)


def ProRateValue(value, inRange, outRange) -> int | float | str:
    return (
        float(value) * (outRange[1] - outRange[0]) / (inRange[1] - inRange[0])
        if (inRange[1] - inRange[0]) != 0 and (outRange[1] - outRange[0]) != 0
        else "Error"
    )


def Bind(val, inRange) -> int:
    return min(inRange[1], max(inRange[0], val))


# TODO - Add Test
def ResizeMaxLength(dim, maxSide) -> tuple:
    val = (dim[0] / dim[1] * maxSide, maxSide)
    val2 = (maxSide, dim[1] / dim[0] * maxSide)
    return val if dim[1] > dim[0] else val2


def Sign(num: int | float) -> int:
    return int(num / abs(num)) if num != 0 else 0
