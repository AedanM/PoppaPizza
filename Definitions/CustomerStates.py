from enum import Enum


class CustomerStates(Enum):
    (
        Null,
        Queuing,
        Seated,
        WaitingForService,
        BeingServed,
        Served,
        LeavingAngry,
        *_,
    ) = range(100)
