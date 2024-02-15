from dataclasses import dataclass

import names

IDCOUNT = 0
FIRSTNAMES = {""}
LASTNAMES = {""}


@dataclass
class Person:
    """Base class for all People Data Classes"""

    FirstName: str
    LastName: str
    IdNum: int
    Body: None = None
    IsAssigned: bool = False

    @classmethod
    def Create(cls, gender="female"):
        """Creates a person object

        Returns-
            Person: Base Person Object
        """
        fName, lName = GenerateName(gender=gender)
        selfid = cls.GenerateID()
        return cls(FirstName=fName, LastName=lName, IdNum=selfid)

    @staticmethod
    def GenerateID() -> int:
        """Generates unique ID for person

        Returns-
            int: Personal ID
        """
        # pylint: disable=global-statement
        global IDCOUNT
        IDCOUNT += 1
        return IDCOUNT


def GenerateName(gender) -> tuple[str, str]:
    global FIRSTNAMES, LASTNAMES
    tryNum = 0
    fName = names.get_first_name(gender=gender)
    while fName in FIRSTNAMES and tryNum < 20:
        fName = names.get_first_name(gender=gender)
        tryNum += 1
    FIRSTNAMES.add(fName)

    tryNum = 0
    lName = names.get_last_name()
    while lName in LASTNAMES and tryNum < 10:
        lName = names.get_last_name()
        tryNum += 1
    LASTNAMES.add(lName)
    return (fName, lName)
