"""Customer States and Speeds"""

from enum import Enum


class CustomerStates(Enum):
    (
        Null,
        WalkingIn,
        FirstInLine,
        Queuing,
        Seated,
        WaitingForService,
        WaitingForSeating,
        BeingServed,
        Served,
        LeavingAngry,
        *_,
    ) = range(100)


QueueStates = [
    CustomerStates.WalkingIn,
    CustomerStates.Queuing,
    CustomerStates.FirstInLine,
]


class MovementSpeeds(Enum):
    Slow: int = 1
    Medium: int = 10
    Fast: int = 100
    Instant: int = 1000
