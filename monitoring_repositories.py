from crontab import CronTab
import helper
import os


def list_repos():
    with open(helper.monitoring_file()) as f:
        print(f.read())


def reset():
    open(helper.recording_file(), "w").close()
    print("Records successfully reset.")


def setup():
    cron = CronTab(user=True)
    job = cron.new(
        command=f"python3 {helper.cronjob_file()}", comment="repository-monitoring"
    )
    job.minute.on(30)
    cron.write()
    print("Cronjob successfully installed.")


def show():
    with open(helper.recording_file()) as f:
        print(f.read())


def start(repo):
    monitoring_file = helper.monitoring_file()
    with open(monitoring_file, helper.access_mode(monitoring_file)) as f:
        for line in f.readlines():
            if repo in line:
                break
        else:
            append_repo(repo)
            print(f"Started monitoring of {repo}")


def append_repo(repo):
    with open(helper.monitoring_file(), "a") as f:
        f.write(repo + "\n")


def stop(repo):
    if not os.path.exists(helper.monitoring_file()):
        print("No Git repositories are being monitored.")
        return

    with open(helper.monitoring_file()) as f:
        lines = f.readlines()
    with open(helper.monitoring_file(), "w") as f:
        for line in lines:
            if line.strip("\n") != repo:
                f.write(line)
    print(f"Stopped monitoring of {repo}")


def teardown():
    cron = CronTab(user=True)
    for job in cron:
        if job.comment == "repository-monitoring":
            cron.remove(job)
            cron.write()
            print("Cronjob successfully removed.")
