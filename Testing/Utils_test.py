from Utilities import Utils
from Testing import TestClass as TC


def test_checkDecimalPercent() -> None:
    testObjects = [
        TC.TestClass(paramList=[100], result=1),
        TC.TestClass(paramList=[0.5], result=0.5),
        TC.TestClass(paramList=[-200], result=-2),
        TC.TestClass(paramList=[-0.2], result=-0.2),
        TC.TestClass(paramList=[(100, 100)], result=(1, 1)),
        TC.TestClass(paramList=[(0.5, 100)], result=(0.5, 100)),
        TC.TestClass(paramList=[(-200, 10.5)], result=(-2, 0.105)),
        TC.TestClass(paramList=[(-0.2, 400)], result=(-0.2, 400)),
    ]
    for test in testObjects:
        testVal = Utils.checkDecimalPercent(val=test.paramList[0])
        try:
            assert testVal == test.result
        except AssertionError:
            print(test, testVal)
            assert False


def test_InRandomVarianceTest() -> None:
    testObjects = [
        TC.TestClass(paramList=[10, 0.5], result=(5, 15)),
        TC.TestClass(paramList=[10, -0.5], result=(5, 15)),
        TC.TestClass(paramList=[-10, 0.5], result=(-15, -5)),
        TC.TestClass(paramList=[-10, -0.5], result=(-15, -5)),
        TC.TestClass(paramList=[10, 50], result=(5, 15)),
        TC.TestClass(paramList=[10, -50], result=(5, 15)),
    ]
    for test in testObjects:
        testVal = Utils.InRandomVariance(
            num=test.paramList[0], percentVariance=test.paramList[1]
        )
        try:
            assert testVal >= test.result[0] and testVal <= test.result[1]
        except AssertionError:
            print(test, testVal)
            assert False


def test_PositionRandomVarianceTest() -> None:
    testObjects = [
        TC.TestClass(
            paramList=[(500, 500), (-10, -10), (1000, 1000)], result=(400, 600)
        ),
        TC.TestClass(paramList=[(500, 500), (10, 10), (1000, 1000)], result=(400, 600)),
        TC.TestClass(
            paramList=[(500, 500), (0.1, 0.1), (1000, 1000)], result=(400, 600)
        ),
        TC.TestClass(
            paramList=[(500, 500), (-0.1, -0.1), (1000, 1000)], result=(400, 600)
        ),
        TC.TestClass(paramList=[(0, 0), (0.1, 0.1), (1000, 1000)], result=(-100, 100)),
    ]
    for test in testObjects:
        try:
            testVal = Utils.PositionRandomVariance(
                position=test.paramList[0],
                percentVarianceTuple=test.paramList[1],
                screenSize=test.paramList[2],
            )
            assert testVal[0] >= test.result[0] and testVal[1] <= test.result[1]
        except AssertionError:
            print(test, testVal)


def test_InTolerance() -> None:
    testObjs = [
        TC.TestClass(result=False, paramList=[0, 100, 10]),
        TC.TestClass(result=False, paramList=[0, -100, 10]),
        TC.TestClass(result=True, paramList=[0, 5, 10]),
        TC.TestClass(result=True, paramList=[0, -5, 10]),
        TC.TestClass(result=False, paramList=[0, 100, -10]),
        TC.TestClass(result=False, paramList=[0, -100, -10]),
        TC.TestClass(result=True, paramList=[0, 0.5, -10]),
        TC.TestClass(result=True, paramList=[0, 5, -10]),
    ]

    for test in testObjs:
        try:
            testVal = Utils.InTolerance(
                num1=test.paramList[0],
                num2=test.paramList[1],
                tolerance=test.paramList[2],
            )
            assert testVal == test.result
        except AssertionError:
            print(test, testVal)
            assert False


def test_InPercentTolerance() -> None:
    testObjs = [
        TC.TestClass(result=True, paramList=[100, 99, 0.05]),
        TC.TestClass(result=True, paramList=[100, 101, 0.05]),
        TC.TestClass(result=True, paramList=[100, 101, -0.05]),
        TC.TestClass(result=True, paramList=[100, 99, -0.05]),
        TC.TestClass(result=False, paramList=[100, 90, 0.05]),
        TC.TestClass(result=False, paramList=[100, 110, 0.05]),
        TC.TestClass(result=False, paramList=[100, 110, -0.05]),
        TC.TestClass(result=False, paramList=[100, 90, -0.05]),
        TC.TestClass(result=True, paramList=[100, 0, 200]),
        TC.TestClass(result=False, paramList=[0, 0, 200]),
    ]
    for test in testObjs:
        try:
            testVal = Utils.InPercentTolerance(
                num1=test.paramList[0],
                num2=test.paramList[1],
                tolerance=test.paramList[2],
            )
            assert testVal == test.result
        except AssertionError:
            print(test, testVal)
            assert False


def test_ProRateValue() -> None:
    testObjs = [
        TC.TestClass(result=20, paramList=[2, (0, 10), (0, 100)]),
        TC.TestClass(result=200, paramList=[20, (0, 10), (0, 100)]),
        TC.TestClass(result=-200, paramList=[-20, (0, 10), (0, 100)]),
        TC.TestClass(result=-20, paramList=[-2, (0, 10), (0, 100)]),
        TC.TestClass(result=2, paramList=[2, (0, 10), (0, 10)]),
        TC.TestClass(result=25, paramList=[2.5, (0, 10), (0, 100)]),
        TC.TestClass(result=-25, paramList=[-2.5, (0, 10), (0, 100)]),
        TC.TestClass(result="Error", paramList=[-2.5, (0, 10), (0, 0)]),
        TC.TestClass(result="Error", paramList=[-2.5, (0, 0), (0, 10)]),
        TC.TestClass(result=2.5, paramList=[-2.5, (0, 10), (0, -10)]),
        TC.TestClass(result=-2.5, paramList=[2.5, (0, 10), (0, -10)]),
    ]
    for test in testObjs:
        try:
            testVal = Utils.ProRateValue(
                value=test.paramList[0],
                inRange=test.paramList[1],
                outRange=test.paramList[2],
            )
            assert testVal == test.result
        except AssertionError:
            print(test, testVal)
            assert False


def test_Bind() -> None:
    testObjs = [
        TC.TestClass(result=100, paramList=[200, (0, 100)]),
        TC.TestClass(result=100, paramList=[100.5, (0, 100)]),
        TC.TestClass(result=0, paramList=[-200, (0, 100)]),
        TC.TestClass(result=0, paramList=[-0.1, (0, 100)]),
        TC.TestClass(result=0, paramList=[0, (0, 100)]),
        TC.TestClass(result=100, paramList=[100, (0, 100)]),
    ]
    for test in testObjs:
        try:
            testVal = Utils.Bind(
                val=test.paramList[0],
                inRange=test.paramList[1],
            )
            assert testVal == test.result
        except AssertionError:
            print(test, testVal)
            assert False


def test_Sign() -> None:
    testObjs = [
        TC.TestClass(result=1, paramList=[100]),
        TC.TestClass(result=1, paramList=[0.5]),
        TC.TestClass(result=0, paramList=[0]),
        TC.TestClass(result=-1, paramList=[-1]),
        TC.TestClass(result=-1, paramList=[-0.5]),
    ]
    for test in testObjs:
        try:
            testVal = Utils.Sign(
                num=test.paramList[0],
            )
            assert testVal == test.result
        except AssertionError:
            print(test, testVal)
            assert False
