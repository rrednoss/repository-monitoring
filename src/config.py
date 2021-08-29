import os
import yaml

from persistence import Persistence


class Configuration(Persistence):
    def __init__(self, file_path=os.environ["HOME"], file_name=".repositories"):
        super().__init__(file_path, file_name)

    def add(self, path):
        """
        Adds a new repository to monitor.

        :param path: the repository absolute path
        """
        config = self.read()
        if path in config:
            return
        with open(self.path(), "w") as f:
            config.append(path)
            yaml.safe_dump(config, f)

    def read(self) -> list:
        """
        Reads the repositories that were previously added by func: `add`

        :return: a list of the currently configured repositories
        """
        if self.exists():
            with open(self.path(), "r") as f:
                config = yaml.safe_load(f)
                return config if config is not None else []

    def remove(self, path):
        """
        Counterpart to func: `add`. Used to remove a repository from the currently configured repositories.

        :param path: the repository absolute path
        """
        config = self.read()
        if path not in config:
            return
        with open(self.path(), "w") as f:
            config.remove(path)
            yaml.safe_dump(config, f)
