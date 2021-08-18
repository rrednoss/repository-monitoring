import datetime
import subprocess


def retrieve_commits(repository, author_email, date):
    since = date - datetime.timedelta(days=1)
    until = date
    return subprocess.run(
        [
            "git",
            "log",
            f"--author={author_email}",
            f"--since={since.strftime('%Y.%m.%d')}",
            f"--until={until.strftime('%Y.%m.%d')}",
            "--pretty=format:%s",
            "--no-merges",
        ],
        cwd=repository,
        capture_output=True,
        text=True,
    ).stdout.strip("\n")


def retrieve_email():
    return subprocess.run(
        ["git", "config", "--get", "user.email"],
        capture_output=True,
        text=True,
    ).stdout.strip("\n")
