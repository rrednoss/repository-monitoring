import os


class Persistence:
    def __init__(self, file_path=os.environ["HOME"], file_name=".persistence"):
        self.file_path = file_path
        self.file_name = file_name
        self._setup()

    def _setup(self):
        os.makedirs(self.file_path, exist_ok=True)
        if not self.exists():
            with open(self.path(), "w") as f:
                f.write("---")

    def exists(self) -> bool:
        return os.path.exists(self.path())

    def path(self) -> str:
        return f"{self.file_path}/{self.file_name}.yaml"

    def reset(self):
        with open(self.path(), "w") as f:
            f.write("---")
