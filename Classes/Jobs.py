"""Class for jobs"""

import random
from dataclasses import dataclass
from enum import Enum

JOBIDCOUNT = 1


class UrgencyRatings(Enum):
    Null, Trivial, Normal, Urgent = range(4)


class JobTypes(Enum):
    Null, Standard, Deluxe = range(3)


@dataclass
class Job:
    Type: JobTypes
    Price: float
    Length: int
    AssignedWorker: int
    JobCustomer: int
    Urgency: UrgencyRatings
    JobId: int

    @classmethod
    def SpawnJob(cls) -> "Job":
        # pylint: disable=global-statement
        global JOBIDCOUNT
        JOBIDCOUNT += 1
        urgency = random.choice(list(UrgencyRatings)[1:])
        jobtype = random.choice(list(JobTypes)[1:])
        length = random.randint(5, 100)
        price = (
            1
            * (random.randint(10, 50) + length)
            * (jobtype.value + 1)
            * (urgency.value + 1)
        )
        assignedWorker = 0
        customer = 0
        job = Job(
            Type=jobtype,
            Price=price,
            Length=length,
            AssignedWorker=assignedWorker,
            JobCustomer=customer,
            Urgency=urgency,
            JobId=JOBIDCOUNT,
        )
        return job

    @staticmethod
    def GetAssignedFromID(jobList, targetID) -> tuple:
        for job in jobList:
            if job.JobId == targetID:
                return (job.AssignedWorker, job.JobCustomer)
        return ()

    def Assign(self, target) -> None:
        if "DesiredJob" in dir(target):
            target.DesiredJob = self
            self.JobCustomer = target.IdNum
        else:
            self.AssignedWorker = target.IdNum
        target.IsAssigned = True
        target.CurrentJobId = self.JobId
