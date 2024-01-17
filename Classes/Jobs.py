"""Class for jobs"""
from dataclasses import dataclass
from enum import Enum
import random

JOBIDCOUNT = 0


class UrgencyRatings(Enum):
    Trivial, Urgent = range(2)


class JobTypes(Enum):
    Standard, Deluxe = range(2)


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
    def SpawnJob(cls):
        global JOBIDCOUNT
        JOBIDCOUNT += 1
        urgency = random.choice(list(UrgencyRatings))
        jobtype = random.choice(list(JobTypes))
        length = random.randint(2, 10)
        price = (
            1
            * (random.randint(10, 50) + length)
            * (jobtype.value + 1)
            * (urgency.value + 1)
        )
        assignedWorker = None
        customer = None
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
    def GetAssignedFromID(jobList, targetID):
        for job in jobList:
            if job.JobId == targetID:
                return [job.AssignedWorker, job.JobCustomer]
        return []

    def Assign(self, target):
        if "DesiredJob" in dir(target):
            target.DesiredJob = self
            self.JobCustomer = target.IdNum
        else:
            self.AssignedWorker = target.IdNum
        target.IsAssigned = True
        target.CurrentJobId = self.JobId
