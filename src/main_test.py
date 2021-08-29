import main
import unittest

from unittest import mock


class TestMain(unittest.TestCase):
    @mock.patch("main.commands")
    def test_handle_args_recordings(self, mock_commands):
        args = StubArgs(recordings=True)
        main.handle_args(args)
        mock_commands.recordings.assert_called()

    @mock.patch("main.commands")
    def test_handle_args_reset(self, mock_commands):
        args = StubArgs(reset=True)
        main.handle_args(args)
        mock_commands.reset.assert_called()

    @mock.patch("main.commands")
    def test_handle_args_setup(self, mock_commands):
        args = StubArgs(setup=True)
        main.handle_args(args)
        mock_commands.setup.assert_called()

    @mock.patch("main.commands")
    def test_handle_args_show(self, mock_commands):
        args = StubArgs(show=True)
        main.handle_args(args)
        mock_commands.show.assert_called()

    @mock.patch("main.commands")
    def test_handle_args_start(self, mock_commands):
        args = StubArgs(start=True)
        main.handle_args(args)
        mock_commands.start.assert_called()

    @mock.patch("main.commands")
    def test_handle_args_stop(self, mock_commands):
        args = StubArgs(stop=True)
        main.handle_args(args)
        mock_commands.stop.assert_called()

    @mock.patch("main.commands")
    def test_handle_args_teardown(self, mock_commands):
        args = StubArgs(teardown=True)
        main.handle_args(args)
        mock_commands.teardown.assert_called()


class StubArgs:
    def __init__(
        self,
        recordings=None,
        reset=None,
        setup=None,
        show=None,
        start=None,
        stop=None,
        teardown=None,
    ):
        self.recordings = recordings
        self.reset = reset
        self.setup = setup
        self.show = show
        self.start = start
        self.stop = stop
        self.teardown = teardown
