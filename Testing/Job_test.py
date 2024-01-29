"""Test Module for Job Functions"""
# pylint: disable=invalid-name

from Classes import Jobs


def test_Job() -> None:
    assert Jobs.Job.SpawnJob() is not None
