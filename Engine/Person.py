from dataclasses import dataclass

import names

IDCOUNT = 0


@dataclass
class Person:
    """Base class for all People Data Classes"""

    FirstName: str
    LastName: str
    IdNum: int
    Body: None = None
    IsAssigned: bool = False

    @classmethod
    def Create(cls) -> "Person":
        """Creates a person object

        Returns-
            Person: Base Person Object
        """
        fName = names.get_first_name(gender="female")
        lName = names.get_last_name()
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
