import os


class Persistence:
    def __init__(self, file_path=os.environ["HOME"], file_name=".monitoring"):
        self.file_path = file_path
        self.file_name = file_name
        self._setup()

    def _folder(self) -> str:
        return self.file_path + "/" + self.file_name

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
