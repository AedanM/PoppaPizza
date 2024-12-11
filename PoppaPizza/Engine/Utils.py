"""Utility functions"""

import math
import random


def InRandomVariance(num: int | float, percentVariance: float) -> float:
    """Returns random num in % variance

    Args-
        num (int | float): Base Number
        percentVariance (float): Percentage to vary by

    Returns-
        float: New Varied Number
    """
    percentVariance = CheckDecimalPercent(percentVariance)
    varyAmount = random.randint(a=-100, b=100) * percentVariance * 0.01 * num  # type:ignore
    return num + varyAmount


def CheckDecimalPercent(val: float) -> float:
    """Normalizes Percentages from 0-100 to 0-1

    Args-
        val (tuple | int | float): input value

    Returns-
        float | tuple: Normalized Output
    """
    return float(val) if abs(val) <= 1 else float(val) / 100


def CheckDecimalPercentTuple(val: tuple[float, float]) -> tuple:
    """Normalizes Tuple Percentages from 0-100 to 0-1

    Args-
        val (tuple | int | float): input value

    Returns-
        float | tuple: Normalized Output
    """
    holdList = []
    percentMod = True if (abs(val[0]) < 1) else False
    for i in val:
        holdList.append(float(i) if percentMod else float(i) / 100)
    return tuple(holdList)


def PositionRandomVariance(
    position: tuple[int, int], percentVariance: tuple[float, float], screenSize: tuple[int, int]
) -> tuple[int, int]:
    """Generates a position in random variance of input

    Args-
        position (tuple): Basse Location
        percentVarianceTuple (tuple): Variance in X and Y direction as a % of screen
        screenSize (tuple): Size of Screen as tuple(width, height)

    Returns-
        tuple[int, int]: Random Position
    """
    percentVariance = CheckDecimalPercentTuple(val=percentVariance)
    varyAmountX = math.ceil(
        (random.randint(-100, 100) * 0.01 * percentVariance[0] * screenSize[0])  # type: ignore
        + position[0]
    )
    varyAmountY = math.ceil(
        (random.randint(-100, 100) * 0.01 * percentVariance[1] * screenSize[1])  # type: ignore
        + position[1]
    )
    out = (
        int(Bind(val=varyAmountX, inRange=(0, screenSize[0]))),
        int(Bind(val=varyAmountY, inRange=(0, screenSize[1]))),
    )
    return out


def InTolerance(num1: int | float, num2: int | float, tolerance: int | float) -> bool:
    """Returns if numbers are wthin a numeric tolerance

    Args-
        num1 (int | float): 1st number
        num2 (int | float): 2nd number
        tolerance (int | float): Range of Acceptance

    Returns-
        bool: Status of Tolerance
    """
    return abs(num1 - num2) <= abs(tolerance)


def InPercentTolerance(num1: int | float, num2: int | float, tolerance: int | float) -> bool:
    """Returns if numbers are wthin a percentage tolerance

    Args-
        num1 (int | float): 1st number
        num2 (int | float): 2nd number
        tolerance (float): Tolerance %

    Returns-
        bool: Status of Tolerance
    """
    if num1 == 0:
        return num1 == num2
    tolerance = CheckDecimalPercent(val=tolerance)

    seperation = abs((num1 - num2) / num1)
    return seperation <= abs(tolerance)


def ProRateValue(
    value: int | float,
    inRange: tuple[int | float, int | float],
    outRange: tuple[int | float, int | float],
) -> int | float | None:
    """Changes the range of a value

    Args-
        value (int | float): _description_
        inRange (tuple): Original Range
        outRange (tuple): New Range

    Returns-
        int | float | None: _description_
    """
    return (
        float(value) * (outRange[1] - outRange[0]) / (inRange[1] - inRange[0])
        if (inRange[1] - inRange[0]) != 0 and (outRange[1] - outRange[0]) != 0
        else None
    )


def Bind(val: int | float, inRange: tuple[int | float, int | float]) -> int | float:
    """Binds a value into a range

    Args-
        val (int | float): Input value
        inRange (tuple): Range to bind to

    Returns-
        int | float: Bound Value
    """
    return min(inRange[1], max(inRange[0], val))


# TODO - Add Test
def ResizeMaxLength(dim: tuple[int, int], maxSide: int) -> tuple:
    """Resize a set of dimensions to a maximum

    Args-
        dim (tuple): Dimensions
        maxSide (int): Max side length

    Returns-
        tuple: New Dimensions
    """
    val = (math.floor(dim[0] / dim[1] * maxSide), maxSide)
    val2 = (maxSide, math.floor(dim[1] / dim[0] * maxSide))
    return val if dim[1] > dim[0] else val2


# TODO - Add Test
def PositionInTolerance(pos1: tuple[int, int], pos2: tuple[int, int], tolerance: int) -> bool:
    """Checks if 2 positions are within a numeric tolerance

    Args-
        pos1 (tuple): Position 1
        pos2 (tuple): Position 2
        tolerance (int | float): Numerical Tolerance

    Returns-
        bool: X in Tolerance and Y in Tolerance
    """
    return InTolerance(num1=pos1[1], num2=pos2[1], tolerance=tolerance) and InTolerance(
        num1=pos1[0], num2=pos2[0], tolerance=tolerance
    )


# TODO - Add Test
def OffsetTuple(inputTuple: tuple[int, int], offset: tuple[int, int]) -> tuple[int, int]:
    """Tuple Addition Funciton

    Args-
        inputTuple (tuple): Input
        offset (tuple| int | float):  Amount to offset by

    Returns-
        tuple: Offset Tuple
    """
    element1 = inputTuple[0] + (offset[0] if isinstance(offset, tuple) else offset)
    element2 = inputTuple[1] + (offset[1] if isinstance(offset, tuple) else offset)
    return (element1, element2)


def Sign(num: int | float) -> int:
    """Return Sign from Value

    Args-
        num (int | float): Input

    Returns-
        int: Sign of Number
    """
    return int(num / abs(num)) if num != 0 else 0


def ScaleToSize(
    value: tuple[int, int],
    newSize: tuple[int, int],
    origSize: tuple[int, int] = (1200, 800),
) -> tuple[int, int]:
    """Scale a set of dimensions to a new screen size

    Args-
        value (tuple): Dimensions
        newSize (tuple): New Screen Size
        origSize (tuple, optional): Old Screen Size. Defaults to StandardDimensions["Medium"].

    Returns-
        tuple: New Dimensions
    """
    return (
        ScaleValToSize(val=value[0], newSize=newSize, oldSize=origSize),
        ScaleValToSize(val=value[1], newSize=newSize, oldSize=origSize),
    )


# TODO - Actually Implement
def ScaleValToSize(
    val: int,
    newSize: tuple[int, int],
    oldSize: tuple[int, int] = (1200, 800),
) -> int:
    return val


def ScaleTuple(
    tupleArg: tuple[int | float, int | float], scale: int | float
) -> tuple[int | float, int | float]:
    """Mutiply scalar by tuple

    Args-
        tupleArg (tuple): input Tuple
        scale (int | float): product

    Returns-
        tuple: Scaled Tuple
    """
    return (tupleArg[0] * scale, tupleArg[1] * scale)
