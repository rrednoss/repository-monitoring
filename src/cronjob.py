import datetime

from config import Configuration
from records import Record

import os
import subprocess
import sys


def path():
    return os.path.realpath(__file__)


def monitor():
    repositories = Configuration("repositories").read()
    if len(repositories) == 0:
        print("There are no repositories configured to be monitored.")
        return

    records = Record("records")
    for repository in repositories:
        branch = retrieve_branch(repository)
        timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
        records.add(repository, branch, timestamp)


def retrieve_branch(repository):
    return subprocess.run(
        ["git", "branch", "--show-current"],
        cwd=repository,
        capture_output=True,
        text=True,
    ).stdout.strip("\n")


if __name__ == "__main__":
    sys.exit(monitor())
