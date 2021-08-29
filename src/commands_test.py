import commands
import unittest

from crontab import CronTab
from unittest import mock


class TestCommands(unittest.TestCase):
    @mock.patch("commands.cronjob")
    @mock.patch.object(CronTab, "write")
    @mock.patch.object(CronTab, "new")
    def test_setup(self, mock_crontab_new, mock_crontab_write, mock_cronjob):
        mock_cronjob.path.return_value = "/some-path"
        commands.setup()
        mock_crontab_new.assert_called_with(
            command="python3 /some-path", comment="repository-monitoring"
        )
        mock_crontab_write.assert_called()

    # TODO: Research at how to mock CronTab.
    # @mock.patch.object(CronTab, "write")
    # @mock.patch.object(CronTab, "remove")
    # @mock.patch("commands.CronTab")
    # def test_teardown(self, mock_crontab, mock_crontab_remove, mock_crontab_write):
    #     with mock.patch.object(CronTab, "__init__"):
    #         commands.teardown()
    #         mock_crontab_remove.assert_called_with("")
    #         mock_crontab_write.assert_called()
