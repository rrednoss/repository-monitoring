from config import Configuration
from crontab import CronTab
from records import Record

import commits
import cronjob
import datetime
import re


def recordings():
    """
    Loops through the recordings and prints them to STDOUT.

    Additionally the user made commits are printed out as well.
    """
    records = Record("records").read()
    for project_key, project_entries in records.items():
        print(project_key)
        for entry_key, entry_values in project_entries.items():
            print("-", entry_key, entry_values)
            user_commits = _get_commits(project_key, entry_key)
            if user_commits and len(user_commits) > 0:
                print(" +", re.sub("\n", "\n + ", user_commits))
        print()


def _get_commits(repository, timestamp):
    timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")
    user_email = commits.retrieve_email()
    return commits.retrieve_commits(repository, user_email, timestamp)


def reset():
    """
    Resets all repository recordings up until now.
    """
    Record("records").reset()
    print("Records successfully reset.")


def setup():
    """
    Installs a cronjob that periodically monitors the configured repositories.

    The cronjob executes src.cronjob as Python script.
    """
    cron = CronTab(user=True)
    job = cron.new(
        command=f"python3 {cronjob.path()}",
        comment="repository-monitoring",
    )
    job.minute.every(30)
    cron.write()
    print("Cronjob successfully installed.")


def show():
    """
    Prints currently configured repositories to STDOUT.
    """
    config = Configuration("repositories")
    print(config.read())


def start(path):
    """
    Starts the (branch) monitoring done through the cronjob.

    :param path: the repository to start monitoring on
    """
    config = Configuration("repositories")
    config.add(path)
    print(f"Started monitoring of {path}")


def stop(path):
    """
    Stops the (branch) monitoring done through the cronjob.

    :param path: the repository to stop monitoring on
    """
    config = Configuration("repositories")
    config.remove(path)
    print(f"Stoped monitoring of {path}")


def teardown():
    """
    Removes the previously installed (see :func: `commands.setup`) cronjob.

    This stops the automatic monitoring of the configured repositories.
    """
    cron = CronTab(user=True)
    for job in cron:
        if job.comment == "repository-monitoring":
            cron.remove(job)
            cron.write()
            print("Cronjob successfully removed.")
