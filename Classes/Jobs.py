from dataclasses import dataclass
from enum import Enum
import random

JobIdCount = 0


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
    def SpawnJob(self):
        global JobIdCount
        JobIdCount += 1
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
            JobId=JobIdCount,
        )
        return job

    @staticmethod
    def GetAssignedFromID(JobList, targetID):
        for job in JobList:
            if job.JobId == targetID:
                return [job.AssignedWorker, job.JobCustomer]
        return []

    def Assign(self, target):
        if "desiredJob" in dir(target):
            target.desiredJob = self
            self.JobCustomer = target.idNum
        else:
            self.AssignedWorker = target.idNum
        target.isAssigned = True
        target.currentJobId = self.JobId
