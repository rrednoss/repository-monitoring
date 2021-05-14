## Repository Monitoring
This small script monitors which branches you had checked out and provides you with a detailed information report.
This might be handy if you need to track the time you've spent working on tickets but can't remember it.

### Prerequisites
These tools must be accessible by your user: Git, Python (preferred in version 3) and pip.

### Installation
```bash
pip install python-crontab
```

### Usage
_Optional:_ To access the script from every location it is recommended to use an alias.
```bash
$ python3 monitoring.py --help
usage: monitoring.py [-h] [--list | --reset | --setup | --show | --start | --stop | --teardown]

Monitors Git branches and commits.

optional arguments:
  -h, --help  show this help message and exit
  --list      lists the currently monitored repositories
  --reset     resets the monitor entries created up to this moment
  --setup     creates a cronjob to monitor the checked out branches
  --show      shows your previously checked out branches and commits
  --start     starts monitoring for this repository (repository-monitoring)
  --stop      stop monitoring for this repository (repository-monitoring)
  --teardown  removes the cronjob that monitored the checked out branches
  
$ python3 monitoring.py --setup
Cronjob successfully installed.

$ python3 monitoring.py --start
Started monitoring of <your_repository>

```