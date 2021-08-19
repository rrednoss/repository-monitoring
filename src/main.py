import argparse
import sys

import commands


def create_cli():
    parser = argparse.ArgumentParser(description="Monitors Git branches and commits.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--recordings",
        action="store_true",
        help="prints the recordings up to this moment",
    )
    group.add_argument(
        "--reset",
        action="store_true",
        help="resets the recordings up to this moment",
    )
    group.add_argument(
        "--setup",
        action="store_true",
        help="creates a cronjob to monitor the repositories",
    )
    group.add_argument(
        "--show",
        action="store_true",
        help="shows the currently configured repositories",
    )
    group.add_argument(
        "--start", help="starts monitoring for this path", metavar="PATH"
    )
    group.add_argument("--stop", help="stop monitoring for this path", metavar="PATH")
    group.add_argument(
        "--teardown",
        action="store_true",
        help="removes the cronjob that monitored the repositories",
    )
    handle_args(parser.parse_args())


def handle_args(args):
    if args.recordings:
        commands.recordings()
    elif args.reset:
        commands.reset()
    elif args.setup:
        commands.setup()
    elif args.show:
        commands.show()
    elif args.start:
        commands.start(args.start)
    elif args.stop:
        commands.stop(args.stop)
    elif args.teardown:
        commands.teardown()
    else:
        print("You must select an argument.")


if __name__ == "__main__":
    sys.exit(create_cli())
