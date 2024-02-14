"""Test Module for Job Functions"""

# pylint: disable=invalid-name

from Classes import GameBase, Jobs, People


def test_Job() -> None:
    job = Jobs.Job.SpawnJob()
    assert job is not None


def test_AssignJob() -> None:
    currentGame = GameBase.MainGame()
    worker, _ = People.Worker.CreateWorker(activeGame=currentGame)
    customer, _ = People.Customer.CreateCustomer(activeGame=currentGame)
    customer.DesiredJob.Assign(target=worker)
    assert (worker.IdNum, customer.IdNum) == customer.DesiredJob.GetAssignedFromID(
        jobList=currentGame.JobList, targetID=customer.DesiredJob.JobId
    )
