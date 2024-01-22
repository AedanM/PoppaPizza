import os

# pylint: disable=wrong-import-position
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "True"
from Testing import Utils_test, People_test, Settings_test, Job_test, Game_test
from Classes import Game

Game.MasterGame = Game.Game(activateScreen=False)
testsToRun = [
    Utils_test.RunAllUtilsTests,
    People_test.RunAllPeopleTests,
    Settings_test.RunAllSettingsTests,
    Job_test.RunAllJobTests,
    Game_test.RunAllGameTests,
]
for testToRun in testsToRun:
    if testToRun():
        print(testToRun.__name__ + " passed")
    else:
        print(testToRun.__name__ + " failed")
