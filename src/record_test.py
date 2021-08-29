import datetime
import os
import unittest

from record import Record


class TestRecord(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.name = "test_file"
        self.record = Record(self.path, self.name)

    def tearDown(self) -> None:
        os.remove(self.record.path())

    def test_add(self):
        # creating the test case
        repository = "/home/rednoss/Documents/Workspace/repository-monitoring"
        branch = "main"
        timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
        self.record.add(repository, branch, timestamp)

        # testing the result
        with open(self.record.path(), "r") as f:
            current_record = f.read()
            self.assertTrue(repository in current_record)
            self.assertTrue(branch in current_record)
            self.assertTrue(timestamp in current_record)

    def test_read(self):
        # creating the test case
        repository = "/home/rednoss/Documents/Workspace/repository-monitoring"
        branch = "main"
        timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
        self.record.add(repository, branch, timestamp)

        # testing the result
        current_record = self.record.read()
        self.assertTrue(repository in current_record)
        self.assertTrue(timestamp in current_record.get(repository))
        self.assertTrue(branch in current_record.get(repository).get(timestamp))
