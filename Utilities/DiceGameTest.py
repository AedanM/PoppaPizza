import random

import Utils
from fuzzywuzzy import fuzz
from pytrivia import Trivia


class RoundBasedGame:
    Rounds: int
    MaxRounds: int = 10
    CurrentRound: int = 1
    OnRoundWin: callable = None
    OnRoundLoss: callable = None
    RoundResult: bool = False
    PresentationMethod: callable = lambda self, s: print(s)

    def __init__(self, rounds) -> None:
        self.Rounds = Utils.Bind(val=rounds, inRange=[0, self.MaxRounds])

    def PlayRound(self) -> None:
        self.PresentationMethod(f"Round {self.CurrentRound}/{self.Rounds}")
        self.CurrentRound += 1

    def PlayGame(self) -> None:
        while self.CurrentRound <= self.Rounds:
            self.PlayRound()
            self.OnRoundWin() if self.RoundResult else self.OnRoundLoss()


class DiceGame(RoundBasedGame):
    Dice: int
    MaxDice: int = 45
    DiceBounds: tuple = (6, 48)

    def __init__(self, rounds, dice) -> None:
        super().__init__(rounds=rounds)
        self.Dice = Utils.Bind(val=dice, inRange=[0, self.MaxDice])

    def PlayRound(self) -> None:
        super().PlayRound()

        markToBeat = random.randint(self.DiceBounds[0], self.DiceBounds[1])
        self.PresentationMethod(f"Mark to Beat is {markToBeat}")

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


class TriviaGame(RoundBasedGame):
    TriviaAPI = Trivia(True)
    QuestionList: list = []

    def GetQuestions(self) -> None:
        responseCode = 100
        while responseCode != 0:
            rawResponse = self.TriviaAPI.request(num_questions=self.Rounds + 1)
            responseCode = rawResponse["response_code"]
            print(responseCode)
        self.QuestionList = rawResponse["results"]

    def PlayRound(self) -> None:
        super().PlayRound()
        question = self.QuestionList[self.CurrentRound - 1]
        self.PresentationMethod(
            f"This question is {question['difficulty'].capitalize()} in the Category {question['category']}"
        )
        skip = input("Play or Skip? ")
        if "s" not in skip:
            correctAnswer = self.PresentQuestion()
            answer = input()
            self.RoundResult = fuzz.token_set_ratio(answer, correctAnswer) > 50
            self.PresentationMethod(
                "Correct" if self.RoundResult else f"Incorrect: {correctAnswer}"
            )

    def PresentQuestion(self) -> str:
        question = self.QuestionList[self.CurrentRound - 1]
        self.PresentationMethod(question["question"])
        answers = question["incorrect_answers"] + [question["correct_answer"]]
        random.shuffle(answers)
        self.PresentationMethod(answers)
        return question["correct_answer"]

    def PlayGame(self) -> None:
        self.GetQuestions()
        super().PlayGame()


DiceGame1 = DiceGame(rounds=5, dice=30)
global Money
Money = 1000


def ChangeMoney(scale) -> None:
    global Money
    Money *= scale
    print(Money)


TriviaGame1 = TriviaGame(rounds=5)
TriviaGame1.OnRoundWin = lambda: ChangeMoney(scale=2)
TriviaGame1.OnRoundLoss = lambda: ChangeMoney(scale=0.5)
TriviaGame1.PlayGame()
