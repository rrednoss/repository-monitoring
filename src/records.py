from persistence import Persistence

import yaml


class Record(Persistence):
    @staticmethod
    def _create_entry(branch, timestamp) -> dict:
        return {f"{timestamp}": f"{branch}"}

    @staticmethod
    def _has_entry(entries, timestamp) -> bool:
        return timestamp in entries

    @staticmethod
    def _has_repository(records, repository) -> bool:
        return False if records.get(repository) is None else True

    def add(self, repository, branch, timestamp):
        """
        Adds a new entry, which is a monitored repository and its branch.

        :param repository: the repository absolute path
        :param branch: the repositories branch
        :param timestamp: the timestamp at which the branch was checked out
        """
        records = self.read()
        if not self._has_repository(records, repository):
            records[repository] = {}
        if not self._has_entry(records[repository], timestamp):
            repository_records = records[repository]
            repository_records[timestamp] = branch
        with open(self.path(), "w") as f:
            yaml.safe_dump(records, f)

    def read(self) -> dict:
        """
        Reads the records that were previously added by func: `add`

        :return: a list of the previously persisted records
        """
        if self.exists():
            with open(self.path(), "r") as f:
                records = yaml.safe_load(f)
                return records if records is not None else {}
