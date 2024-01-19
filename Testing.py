import os

# pylint: disable=wrong-import-position
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "True"
from Testing import Utils_test, People_test
from Classes import Game

Game.MasterGame = Game.Game(activateScreen=False)
testsToRun = [Utils_test.RunAllUtilsTests, People_test.RunAllPeopleTests]
for testToRun in testsToRun:
    if testToRun():
        print(testToRun.__name__ + " passed")
    else:
        print(testToRun.__name__ + " failed")
