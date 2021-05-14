import argparse
import monitoring_repositories
import os
import sys


def main():
    parser = argparse.ArgumentParser(description="Monitors Git branches and commits.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--list", action="store_true", help="lists the currently monitored repositories")
    group.add_argument("--reset", action="store_true", help="resets the monitor entries created up to this moment")
    group.add_argument("--setup", action="store_true", help="creates a cronjob to monitor the checked out branches")
    group.add_argument("--show", action="store_true", help="shows your previously checked out branches and commits")
    group.add_argument("--start", action="store_true",
                       help=f"starts monitoring for this repository ({get_repo_name()})")
    group.add_argument("--stop", action="store_true",
                       help=f"stop monitoring for this repository ({get_repo_name()})")
    group.add_argument("--teardown", action="store_true",
                       help="removes the cronjob that monitored the checked out branches")

    handle_args(parser.parse_args())


def get_repo_name():
    if is_valid_repo():
        working_directory = os.getcwd()
        return working_directory.split("/")[-1]
    else:
        return "invalid - no git repository"


def is_valid_repo():
    hidden_git_folder = os.getcwd() + "/.git"
    return os.path.exists(hidden_git_folder)


def handle_args(args):
    if args.list:
        monitoring_repositories.list_repos()
    elif args.reset:
        monitoring_repositories.reset()
    elif args.setup:
        monitoring_repositories.setup()
    elif args.show:
        monitoring_repositories.show()
    elif args.start:
        monitoring_repositories.start(os.getcwd())
    elif args.stop:
        monitoring_repositories.stop(os.getcwd())
    elif args.teardown:
        monitoring_repositories.teardown()


if __name__ == '__main__':
    sys.exit(main())
