import os


class Persistence:
    def __init__(self, file_name):
        self.file_name = file_name
        self._setup()

    @staticmethod
    def _folder() -> str:
        return os.environ["HOME"] + "/.monitoring"  # Make this folder configurable?

    def _setup(self):
        os.makedirs(self._folder(), exist_ok=True)
        if not self.exists():
            with open(self.path(), "w") as f:
                f.write("---")

    def exists(self) -> bool:
        return os.path.exists(self.path())

    def path(self) -> str:
        return self._folder() + f"/{self.file_name}.yaml"

    def reset(self):
        with open(self.path(), "w") as f:
            f.write("---")
