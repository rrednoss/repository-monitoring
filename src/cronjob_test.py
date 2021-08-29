import cronjob
import unittest

from config import Configuration
from persistence import Persistence
from record import Record
from unittest import mock


class TestCronjob(unittest.TestCase):
    @mock.patch("cronjob.retrieve_branch")
    @mock.patch.object(Record, "add")
    @mock.patch.object(Configuration, "read")
    def test_monitor(self, mock_conf, mock_record, mock_retrieve):
        with mock.patch.object(Persistence, "__init__", lambda x, y, z: None):
            mock_conf.return_value = ["/home/username/repo"]
            mock_retrieve.return_value = "main"

            cronjob.monitor()
            mock_record.assert_called_with("/home/username/repo", "main", mock.ANY)

    @mock.patch("commits.subprocess.run")
    def test_retrieve_email(self, mock_run):
        type(mock_run.return_value).stdout = mock.PropertyMock(
            return_value="main\n"
        )
        self.assertEqual("main", cronjob.retrieve_branch("/home/username/repo"))


if __name__ == "__main__":
    unittest.main()
