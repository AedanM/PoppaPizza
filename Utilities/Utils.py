"""Utilites"""
import math
import random


def InRandomVarianpypyce(num, percentVariance) -> float:
    percentVariance = CheckDecimalPercent(percentVariance)
    varyAmount = random.randint(a=-100, b=100) * percentVariance * 0.01 * num
    return num + varyAmount


def CheckDecimalPercent(val) -> float | tuple:
    returnVal = None
    if isinstance(val, tuple):
        holdList = []
        percentMod = True if (abs(val[0]) < 1) else False
        for i in val:
            holdList.append(float(i) if percentMod else float(i) / 100)
        returnVal = tuple(holdList)
    else:
        returnVal = float(val) if abs(val) <= 1 else float(val) / 100
    return returnVal


def PositionRandomVariance(
    position, percentVarianceTuple, screenSize
) -> tuple[int, int]:
    percentVarianceTuple = CheckDecimalPercent(val=percentVarianceTuple)
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
    tolerance = CheckDecimalPercent(val=tolerance)
    if num1 == 0:
        return False
    seperation = abs((num1 - num2) / num1)
    return seperation <= abs(tolerance)


def ProRateValue(value, inRange, outRange) -> int | float | None:
    return (
        float(value) * (outRange[1] - outRange[0]) / (inRange[1] - inRange[0])
        if (inRange[1] - inRange[0]) != 0 and (outRange[1] - outRange[0]) != 0
        else None
    )


def Bind(val, inRange) -> int:
    return min(inRange[1], max(inRange[0], val))


# TODO - Add Test
def ResizeMaxLength(dim, maxSide) -> tuple:
    val = (math.floor(dim[0] / dim[1] * maxSide), maxSide)
    val2 = (maxSide, math.floor(dim[1] / dim[0] * maxSide))
    return val if dim[1] > dim[0] else val2


# TODO - Add Test
def PositionInTolerance(pos1, pos2, tolerance) -> bool:
    return InTolerance(num1=pos1[1], num2=pos2[1], tolerance=tolerance) and InTolerance(
        num1=pos1[0], num2=pos2[0], tolerance=tolerance
    )


def Sign(num: int | float) -> int:
    return int(num / abs(num)) if num != 0 else 0
