import math
import random
import threading
from enum import Enum

from pytrivia import Trivia

from Classes import GameBase, Sprite, Writing
from Definitions import ColorDefines, DefinedLocations
from Engine import RoundBasedGame, Utils


class GameMode(Enum):
    (Base, DiceGame, TriviaGame, *_) = range(10)


class GameStates(Enum):
    (
        Loading,
        Start,
        PlayOrSkip,
        Questions,
        Wait,
        CorrectAnswer,
        IncorrectAnswer,
        End,
        Exit,
        *_,
    ) = range(10)


class TriviaGame(RoundBasedGame.RoundBasedGame):
    TriviaAPI = Trivia(True)
    QuestionList: list = []
    DisplayedText = {
        "Round Text": Writing.TextBox(
            center=DefinedLocations.LocationDefs.TriviaRoundText,
            font=Writing.DefinedFonts["Datetime"],
        ),
        "Title Text": Writing.TextBox(
            center=DefinedLocations.LocationDefs.TriviaTitleText,
            text="Trivia Minigame",
            font=Writing.DefinedFonts["Titles"],
        ),
        "Main Text L1": Writing.TextBox(
            center=DefinedLocations.LocationDefs.TriviaMainText,
            font=Writing.DefinedFonts["Trivia Game"],
        ),
        "Main Text L2": Writing.TextBox(
            center=Utils.OffsetTuple(
                inputTuple=DefinedLocations.LocationDefs.TriviaMainText,
                offset=(0, 48),
            ),
            font=Writing.DefinedFonts["Trivia Game"],
        ),
        "Minor Text": Writing.TextBox(
            center=DefinedLocations.LocationDefs.TriviaMinorText
        ),
    }

    def __init__(self, rounds, activeGame) -> None:
        super().__init__(rounds=rounds, activeGame=activeGame)
        self.GameState = GameStates.Loading
        self.BackgroundColor = ColorDefines.TriviaBlue
        questionThread = threading.Thread(target=self.GetQuestions)
        self.StartingCash = activeGame.UserInventory.Money
        self.CurrentCash = activeGame.UserInventory.Money
        questionThread.start()

    def UpdateStateMachine(self, inputStr) -> None:
        super().UpdateStateMachine(inputStr=inputStr)
        match inputStr:
            case "":
                pass
            case "Loading Questions":
                self.GameState = GameStates.Start
            case "Begin":
                self.GameState = GameStates.PlayOrSkip
            case "Play":
                self.GameState = GameStates.Questions
            case "Skip":
                self.CurrentRound += 1
            case "Exit":
                self.GameState = GameStates.Exit
            case "Continue":
                self.CurrentRound += 1
                self.GameState = GameStates.PlayOrSkip
            case other:
                answer = self.QuestionList[self.CurrentRound - 1]["Correct Answer"]
                self.GameState = (
                    GameStates.CorrectAnswer
                    if other == answer
                    else GameStates.IncorrectAnswer
                )
        if self.CurrentRound > self.Rounds and self.GameState != GameStates.Exit:
            self.GameState = GameStates.End
            self.CurrentRound = self.Rounds

    def GetQuestions(self) -> None:
        responseCode = 100
        while responseCode != 0:
            rawResponse = self.TriviaAPI.request(num_questions=self.Rounds + 1)
            responseCode = rawResponse["response_code"]
        results = rawResponse["results"]
        for question in results:
            questionDict = {}
            questionDict["Question"] = question["question"]
            questionDict["Difficulty"] = question["difficulty"]
            questionDict["Category"] = question["category"]
            questionDict["Answers"] = question["incorrect_answers"] + [
                question["correct_answer"]
            ]
            random.shuffle(questionDict["Answers"])
            questionDict["Correct Answer"] = question["correct_answer"]
            self.QuestionList.append(questionDict)

    def PopulateButtons(self, textList) -> None:
        self.MasterSpriteGroup.empty()
        for textBox in [
            value for key, value in self.DisplayedText.items() if "Button" in key
        ]:
            textBox.Text = ""
        answerLocations = DefinedLocations.LocationDefs.Answers(num=len(textList))
        for idx, text in enumerate(textList):
            self.DisplayedText[f"Button {idx}"] = Writing.TextBox(
                center=answerLocations[idx],
                text=text,
                font=Writing.DefinedFonts["Trivia Answers"],
            )

            self.MasterSpriteGroup.add(
                Sprite.ButtonObject(
                    position=answerLocations[idx],
                    backColor=ColorDefines.TriviaBlue,
                    size=(400, 150) if self.QuestionList else (600, 150),
                )
            )

    def StartGame(self) -> None:
        self.DisplayedText["Main Text L1"].Text = "Press to Begin"
        self.PopulateButtons(
            textList=["Begin" if self.QuestionList else "Loading Questions"]
        )

    def PlayOrSkip(self) -> None:
        question = self.QuestionList[self.CurrentRound - 1]
        self.DisplayedText["Main Text L1"].Text = (
            f"This question is ranked {question['Difficulty']}"
        )
        self.DisplayedText["Main Text L2"].Text = f"Category is {question['Category']}"
        self.PopulateButtons(
            textList=["Play", "Skip"],
        )
        self.GameState = GameStates.Wait

    # TODO - Fix wordwrap
    def PresentQuestion(self):
        question = self.QuestionList[self.CurrentRound - 1]
        if len(question["Question"]) < 50:
            self.DisplayedText["Main Text L1"].Text = question["Question"]
            self.DisplayedText["Main Text L2"].Text = ""
        else:
            self.DisplayedText["Main Text L1"].Text = question["Question"][:25]
            self.DisplayedText["Main Text L2"].Text = question["Question"][25:]
        # TODO- fix buttons to text size
        self.PopulateButtons(textList=question["Answers"])
        self.GameState = GameStates.Wait

    def Results(self) -> None:
        scale = 1
        match self.QuestionList[self.CurrentRound - 1]["Difficulty"]:
            case "hard":
                scale = 2
            case "medium":
                scale = 1.5
            case "easy":
                scale = 1.25

        if self.GameState is GameStates.CorrectAnswer:
            self.DisplayedText["Main Text L1"].Text = (
                f"Correct! You have earned ${((self.CurrentCash * scale) - self.CurrentCash):.2f}"
            )
            self.DisplayedText["Main Text L2"].Text = ""
            self.ResultsList.append(True)
            self.CurrentCash *= scale
        else:
            self.DisplayedText["Main Text L1"].Text = (
                f"Incorrect! You have lost ${abs((self.CurrentCash / scale) - self.CurrentCash):.2f}"
            )
            self.DisplayedText["Main Text L2"].Text = (
                f"Correct Answer was {self.QuestionList[self.CurrentRound -1]['Correct Answer']}"
            )
            self.ResultsList.append(False)
            self.CurrentCash /= scale

        self.PopulateButtons(textList=["Continue"])
        self.GameState = GameStates.Wait

    def Summary(self) -> None:
        self.DisplayedText["Main Text L1"].Text = (
            f"You answered {len([x for x in self.ResultsList if x])}/{len(self.ResultsList)} correctly and skipped {self.Rounds - len(self.ResultsList)}"
        )
        deltaMoney = self.CurrentCash - self.StartingCash
        descriptor = "earnings" if deltaMoney > 0 else "losses"
        self.DisplayedText["Main Text L2"].Text = (
            f"Resulting in total {descriptor} ${abs(deltaMoney):.2f}"
        )
        self.PopulateButtons(textList=["Exit"])
        self.GameState = GameStates.Wait

    def StartRound(self) -> None:
        super().StartRound()

        match self.GameState:
            case GameStates.Loading | GameStates.Start:
                self.StartGame()
            case GameStates.PlayOrSkip:
                self.PlayOrSkip()
            case GameStates.Questions:
                self.PresentQuestion()
            case GameStates.IncorrectAnswer:
                self.Results()
            case GameStates.CorrectAnswer:
                self.Results()
            case GameStates.End:
                self.Summary()
            case GameStates.Exit:
                GameBase.MasterGame.ClearMiniGame()
            case other:
                pass

        for text in self.DisplayedText.values():
            text.Rect = text.WriteToScreen(activeScreen=self.Screen)

    def PlayGame(self) -> None:
        super().PlayGame()


def MakeTriviaGame(activeGame) -> None:
    activeGame.GameClock.SetRunning(False)
    activeGame.MiniGame = TriviaGame(rounds=5, activeGame=activeGame)
    activeGame.Mode = GameMode.TriviaGame


class DiceGame(RoundBasedGame.RoundBasedGame):
    Dice: int
    MaxDice: int = 45
    DiceBounds: tuple = (6, 48)

    def __init__(self, rounds, dice, activeGame) -> None:
        super().__init__(rounds=rounds, activeGame=activeGame)
        self.Dice = math.floor(Utils.Bind(val=dice, inRange=[0, self.MaxDice]))

    def StartRound(self) -> None:
        super().StartRound()

        markToBeat = random.randint(self.DiceBounds[0], self.DiceBounds[1])
        self.DisplayedText["Main Text"].Text = f"Mark to Beat is {markToBeat}"

        numDice = self.GetDiceCount() if self.Dice > 0 else 0
        self.Dice -= numDice
        diceSum = self.MakeDiceRoll(numDice=numDice)

    def GetDiceCount(self) -> int:
        numDice = input(
            f"How many dice would you like to use? ({self.Dice} remaining) "
        )
        while not numDice.isnumeric() or int(numDice) > self.Dice:
            numDice = input(f"Invalid Choice: ")
        return int(numDice)

    def MakeDiceRoll(self, numDice) -> int:
        diceTotal = 0
        for i in range(numDice):
            diceRoll = random.randint(1, 6)
            diceTotal += diceRoll
            print(f"Die {i} rolled {diceRoll}")
        print(
            f"Total for round is {diceTotal}"
            if diceTotal != 0
            else "Round is forfeit without dice"
        )
        return diceTotal
