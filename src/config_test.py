import os
import unittest

from config import Configuration


class TestConfig(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.name = "test_file"
        self.config = Configuration(self.path, self.name)

    def tearDown(self) -> None:
        os.remove(self.config.path())

    def test_add(self):
        expected = "/home/rednoss/Documents/Workspace/repository-monitoring"
        self.config.add(expected)

        with open(self.config.path(), "r") as f:
            self.assertEqual(f"- {expected}\n", f.read())

    def test_read(self):
        path = "/home/rednoss/Documents/Workspace/repository-monitoring"
        self.config.add(path)
        self.assertEqual(str(self.config.read()), f"['{path}']")

    def test_remove(self):
        path = "/home/rednoss/Documents/Workspace/repository-monitoring"
        self.config.add(path)
        self.config.remove(path)

        with open(self.config.path(), "r") as f:
            self.assertEqual("[]\n", str(f.read()))


if __name__ == "__main__":
    unittest.main()