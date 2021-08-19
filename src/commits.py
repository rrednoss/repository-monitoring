import datetime
import subprocess


def retrieve_commits(repository, author_email, date) -> str:
    """
    Uses the Git command to retrieve the user commits on a specific date.

    :param repository: The repository git call 'git log' in.
    :param author_email: The author to filter the commits.
    :param date: The date on which the commits are retrieved.
    :return: The commits returned as string and seperated by "\n".
    """
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


def retrieve_email() -> str:
    """
    Uses the Git command to retrieve the current configured user email address.

    :return: The global configured user email.
    """
    return subprocess.run(
        ["git", "config", "--get", "user.email"],
        capture_output=True,
        text=True,
    ).stdout.strip("\n")
