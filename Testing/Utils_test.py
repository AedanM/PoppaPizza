"""Test Module for Utils"""

# pylint: disable=invalid-name

from Engine import Utils
from Testing import TestClass as TC


def test_checkDecimalPercent() -> None:
    testObjects = [
        TC.TestClass(ParamList=[100], Result=1),
        TC.TestClass(ParamList=[0.5], Result=0.5),
        TC.TestClass(ParamList=[-200], Result=-2),
        TC.TestClass(ParamList=[-0.2], Result=-0.2),
        TC.TestClass(ParamList=[(100, 100)], Result=(1, 1)),
        TC.TestClass(ParamList=[(0.5, 100)], Result=(0.5, 100)),
        TC.TestClass(ParamList=[(-200, 10.5)], Result=(-2, 0.105)),
        TC.TestClass(ParamList=[(-0.2, 400)], Result=(-0.2, 400)),
    ]
    for test in testObjects:
        testVal = Utils.CheckDecimalPercent(val=test.ParamList[0])
        try:
            assert testVal == test.Result
        except AssertionError:
            print(test, testVal)
            assert False


def test_InRandomVarianceTest() -> None:
    testObjects = [
        TC.TestClass(ParamList=[10, 0.5], Result=(5, 15)),
        TC.TestClass(ParamList=[10, -0.5], Result=(5, 15)),
        TC.TestClass(ParamList=[-10, 0.5], Result=(-15, -5)),
        TC.TestClass(ParamList=[-10, -0.5], Result=(-15, -5)),
        TC.TestClass(ParamList=[10, 50], Result=(5, 15)),
        TC.TestClass(ParamList=[10, -50], Result=(5, 15)),
    ]
    for test in testObjects:
        testVal = Utils.InRandomVariance(num=test.ParamList[0], percentVariance=test.ParamList[1])
        try:
            assert testVal >= test.Result[0] and testVal <= test.Result[1]
        except AssertionError:
            print(test, testVal)
            assert False


def test_PositionRandomVarianceTest() -> None:
    testObjects = [
        TC.TestClass(ParamList=[(500, 500), (-10, -10), (1000, 1000)], Result=(400, 600)),
        TC.TestClass(ParamList=[(500, 500), (10, 10), (1000, 1000)], Result=(400, 600)),
        TC.TestClass(ParamList=[(500, 500), (0.1, 0.1), (1000, 1000)], Result=(400, 600)),
        TC.TestClass(ParamList=[(500, 500), (-0.1, -0.1), (1000, 1000)], Result=(400, 600)),
        TC.TestClass(ParamList=[(0, 0), (0.1, 0.1), (1000, 1000)], Result=(-100, 100)),
    ]
    for test in testObjects:
        try:
            testVal = Utils.PositionRandomVariance(
                position=test.ParamList[0],
                percentVariance=test.ParamList[1],
                screenSize=test.ParamList[2],
            )
            assert testVal[0] >= test.Result[0] and testVal[1] <= test.Result[1]
        except AssertionError:
            print(test, testVal)


def test_InTolerance() -> None:
    testObjs = [
        TC.TestClass(Result=False, ParamList=[0, 100, 10]),
        TC.TestClass(Result=False, ParamList=[0, -100, 10]),
        TC.TestClass(Result=True, ParamList=[0, 5, 10]),
        TC.TestClass(Result=True, ParamList=[0, -5, 10]),
        TC.TestClass(Result=False, ParamList=[0, 100, -10]),
        TC.TestClass(Result=False, ParamList=[0, -100, -10]),
        TC.TestClass(Result=True, ParamList=[0, 0.5, -10]),
        TC.TestClass(Result=True, ParamList=[0, 5, -10]),
    ]

    for test in testObjs:
        try:
            testVal = Utils.InTolerance(
                num1=test.ParamList[0],
                num2=test.ParamList[1],
                tolerance=test.ParamList[2],
            )
            assert testVal == test.Result
        except AssertionError:
            print(test, testVal)
            assert False


def test_InPercentTolerance() -> None:
    testObjs = [
        TC.TestClass(Result=True, ParamList=[100, 99, 0.05]),
        TC.TestClass(Result=True, ParamList=[100, 101, 0.05]),
        TC.TestClass(Result=True, ParamList=[100, 101, -0.05]),
        TC.TestClass(Result=True, ParamList=[100, 99, -0.05]),
        TC.TestClass(Result=False, ParamList=[100, 90, 0.05]),
        TC.TestClass(Result=False, ParamList=[100, 110, 0.05]),
        TC.TestClass(Result=False, ParamList=[100, 110, -0.05]),
        TC.TestClass(Result=False, ParamList=[100, 90, -0.05]),
        TC.TestClass(Result=True, ParamList=[100, 0, 200]),
        TC.TestClass(Result=False, ParamList=[0, 0, 200]),
    ]
    for test in testObjs:
        try:
            testVal = Utils.InPercentTolerance(
                num1=test.ParamList[0],
                num2=test.ParamList[1],
                tolerance=test.ParamList[2],
            )
            assert testVal == test.Result
        except AssertionError:
            print(test, testVal)
            assert False


def test_ProRateValue() -> None:
    testObjs = [
        TC.TestClass(Result=20, ParamList=[2, (0, 10), (0, 100)]),
        TC.TestClass(Result=200, ParamList=[20, (0, 10), (0, 100)]),
        TC.TestClass(Result=-200, ParamList=[-20, (0, 10), (0, 100)]),
        TC.TestClass(Result=-20, ParamList=[-2, (0, 10), (0, 100)]),
        TC.TestClass(Result=2, ParamList=[2, (0, 10), (0, 10)]),
        TC.TestClass(Result=25, ParamList=[2.5, (0, 10), (0, 100)]),
        TC.TestClass(Result=-25, ParamList=[-2.5, (0, 10), (0, 100)]),
        TC.TestClass(Result="Error", ParamList=[-2.5, (0, 10), (0, 0)]),
        TC.TestClass(Result="Error", ParamList=[-2.5, (0, 0), (0, 10)]),
        TC.TestClass(Result=2.5, ParamList=[-2.5, (0, 10), (0, -10)]),
        TC.TestClass(Result=-2.5, ParamList=[2.5, (0, 10), (0, -10)]),
    ]
    for test in testObjs:
        try:
            testVal = Utils.ProRateValue(
                value=test.ParamList[0],
                inRange=test.ParamList[1],
                outRange=test.ParamList[2],
            )
            assert testVal == test.Result
        except AssertionError:
            print(test, testVal)
            assert False


def test_Bind() -> None:
    testObjs = [
        TC.TestClass(Result=100, ParamList=[200, (0, 100)]),
        TC.TestClass(Result=100, ParamList=[100.5, (0, 100)]),
        TC.TestClass(Result=0, ParamList=[-200, (0, 100)]),
        TC.TestClass(Result=0, ParamList=[-0.1, (0, 100)]),
        TC.TestClass(Result=0, ParamList=[0, (0, 100)]),
        TC.TestClass(Result=100, ParamList=[100, (0, 100)]),
    ]
    for test in testObjs:
        try:
            testVal = Utils.Bind(
                val=test.ParamList[0],
                inRange=test.ParamList[1],
            )
            assert testVal == test.Result
        except AssertionError:
            print(test, testVal)
            assert False


def test_Sign() -> None:
    testObjs = [
        TC.TestClass(Result=1, ParamList=[100]),
        TC.TestClass(Result=1, ParamList=[0.5]),
        TC.TestClass(Result=0, ParamList=[0]),
        TC.TestClass(Result=-1, ParamList=[-1]),
        TC.TestClass(Result=-1, ParamList=[-0.5]),
    ]
    for test in testObjs:
        try:
            testVal = Utils.Sign(
                num=test.ParamList[0],
            )
            assert testVal == test.Result
        except AssertionError:
            print(test, testVal)
            assert False


def test_ResizeMaxLength() -> None:
    testObjs = [
        TC.TestClass(Result=(50, 50), ParamList=[(100, 100), 50]),
        TC.TestClass(Result=(50, 33), ParamList=[(150, 100), 50]),
        TC.TestClass(Result=(33, 50), ParamList=[(100, 150), 50]),
        TC.TestClass(Result=(25, 50), ParamList=[(200, 400), 50]),
        TC.TestClass(Result=(50, 50), ParamList=[(10, 10), 50]),
        TC.TestClass(Result=(50, 25), ParamList=[(20, 10), 50]),
        TC.TestClass(Result=(25, 50), ParamList=[(10, 20), 50]),
    ]
    for test in testObjs:
        try:
            testVal = Utils.ResizeMaxLength(dim=test.ParamList[0], maxSide=test.ParamList[1])
            assert testVal == test.Result
        except AssertionError:
            print(test, testVal)
            assert False
