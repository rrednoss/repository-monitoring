import commits
import datetime
import unittest

from unittest import mock


class TestCommits(unittest.TestCase):
    @mock.patch("commits.subprocess")
    def test_retrieve_commits_params(self, mock_subprocess):
        commits.retrieve_commits(
            "/home/username",
            "non-existing@renerednoss.de",
            datetime.datetime(2000, 1, 1, 23, 59),
        )
        mock_subprocess.run.assert_called_with(
            [
                "git",
                "log",
                "--author=non-existing@renerednoss.de",
                "--since=1999.12.31",
                "--until=2000.01.01",
                "--pretty=format:%s",
                "--no-merges",
            ],
            cwd="/home/username",
            capture_output=True,
            text=True,
        )

    @mock.patch("commits.subprocess.run")
    def test_retrieve_commits(self, mock_run):
        type(mock_run.return_value).stdout = mock.PropertyMock(
            return_value="ID-0 New super cool feature!\n"
        )
        actual = commits.retrieve_commits("", "", datetime.datetime(2000, 1, 1, 23, 59))
        self.assertEqual("ID-0 New super cool feature!", actual)

    @mock.patch("commits.subprocess.run")
    def test_retrieve_email(self, mock_run):
        type(mock_run.return_value).stdout = mock.PropertyMock(
            return_value="non-existing@renerednoss.de\n"
        )
        self.assertEqual("non-existing@renerednoss.de", commits.retrieve_email())


if __name__ == "__main__":
    unittest.main()
