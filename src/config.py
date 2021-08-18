from persistence import Persistence

import yaml


class Configuration(Persistence):
    def add(self, path):
        config = self.read()
        if path in config:
            return
        with open(self.path(), "w") as f:
            config.append(path)
            yaml.safe_dump(config, f)

    def read(self) -> list:
        if self.exists():
            with open(self.path(), "r") as f:
                config = yaml.safe_load(f)
                return config if config is not None else []

    def remove(self, path):
        config = self.read()
        if path not in config:
            return
        with open(self.path(), "w") as f:
            config.remove(path)
            yaml.safe_dump(config, f)
