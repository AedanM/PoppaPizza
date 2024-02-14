"""Class for jobs"""

import random
from dataclasses import dataclass
from enum import Enum

JOBIDCOUNT = 1


class UrgencyRatings(Enum):
    """Rating of how quickly a job must be done"""

    Null, Trivial, Normal, Urgent = range(4)


class JobTypes(Enum):
    """Rating of different job value levels"""

    Null, Standard, Deluxe = range(3)


@dataclass
class Job:
    """Class for Customer Jobs"""

    Type: JobTypes
    Price: float
    Length: int
    AssignedWorker: int
    JobCustomer: int
    Urgency: UrgencyRatings
    JobId: int

    @classmethod
    def SpawnJob(cls) -> "Job":
        """Create a Job

        Returns-
            Job: Generated Job
        """
        # pylint: disable=global-statement
        global JOBIDCOUNT
        JOBIDCOUNT += 1
        urgency = random.choice(list(UrgencyRatings)[1:])
        jobtype = random.choice(list(JobTypes)[1:])
        length = random.randint(5, 100)
        price = 1 * (random.randint(10, 25)) * (jobtype.value + 1) * (urgency.value + 1)
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
        """Find assigned people to job

        Args-
            jobList (list): Master list of jobs
            targetID (_type_): ID of job to lookup

        Returns-
            tuple: (Assigned Worker, Assigned Customer)
        """
        assignedMems = [
            (job.AssignedWorker, job.JobCustomer)
            for job in jobList
            if job.JobId == targetID
        ]
        if assignedMems:
            return assignedMems[0]
        return ()

    def Assign(self, target) -> None:
        """Assign Job to Person
            If customer then the job is placed given to them as their desired
        Args-
            target (Person): Person to assign job to
        """
        if "DesiredJob" in dir(target):
            target.DesiredJob = self
            self.JobCustomer = target.IdNum
        else:
            self.AssignedWorker = target.IdNum
        target.IsAssigned = True
        target.CurrentJobId = self.JobId
