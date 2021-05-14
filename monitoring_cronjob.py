import datetime
import helper
import os
import subprocess
import sys

from monitoring import handle_args


def main():
    if not os.path.exists(helper.monitoring_file()):
        print("No Git repositories are being monitored.")
        return

    with open(helper.monitoring_file()) as f:
        for line in f.readlines():
            repo = line.strip("\n")
            branch = get_branch(repo)
            record(repo.split("/")[-1], branch)


def get_branch(repo):
    return subprocess.run(
        ["git", "branch", "--show-current"],
        cwd=repo,
        capture_output=True,
        text=True
    ).stdout.strip("\n")


def record(repo, branch):
    recording = f"{datetime.datetime.now().strftime('%d.%m.%Y')} {repo} {branch}\n"
    recording_file = helper.recording_file()
    with open(recording_file, helper.access_mode(recording_file)) as f:
        for line in f.readlines():
            if recording in line:
                break
        else:
            append_record(recording)


def append_record(recording):
    with open(helper.recording_file(), "a") as f:
        f.write(recording)


if __name__ == '__main__':
    sys.exit(main())
