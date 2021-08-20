import unittest
import os

from persistence import Persistence


class TestPersistence(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.name = "test_file"
        self.persistence = Persistence(self.path, self.name)

    def tearDown(self) -> None:
        os.remove(self.persistence.path())

    def test_exists(self):
        self.assertTrue(self.persistence.exists())

    def test_path(self):
        expected = f"{self.path}/{self.name}.yaml"
        actual = self.persistence.path()
        self.assertEqual(expected, actual)

    def test_reset(self):
        with open(self.persistence.path(), "w") as f:
            f.write("My best joke!")
        self.persistence.reset()
        with open(self.persistence.path(), "r") as f:
            self.assertEqual("---", f.read())


if __name__ == "__main__":
    unittest.main()
