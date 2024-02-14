"""Customer States and Speeds"""

from enum import Enum


# TODO - Use this to reshape CustomerHandler
class CustomerStates(Enum):
    """Enum of Customer States"""

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
