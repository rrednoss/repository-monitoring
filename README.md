## Repository Monitoring
This small script monitors which branches you had checked out and provides you with a detailed information report.
This might be handy if you need to track the time you've spent working on tickets but can't remember it.

### Prerequisites
These tools must be accessible by your user: Git, Python (preferred in version 3) and pip.

Since this script uses a cronjob internally, it requires UNIX-based systems.

### Installation
```bash
pip3 install -r requirements.txt
```

### Usage
_Optional:_ To access the script from every location it is recommended to use an alias.
```bash
$ python3 src/main.py --help
usage: main.py [-h] [--recordings | --reset | --setup | --show | --start PATH | --stop PATH | --teardown]

Monitors Git branches and commits.

optional arguments:
  -h, --help    show this help message and exit
  --recordings  prints the recordings up to this moment
  --reset       resets the recordings up to this moment
  --setup       creates a cronjob to monitor the repositories
  --show        shows the currently configured repositories
  --start PATH  starts monitoring for this path
  --stop PATH   stop monitoring for this path
  --teardown    removes the cronjob that monitored the repositories

  
$ python3 src/main.py --setup
Cronjob successfully installed.

$ python3 src/main.py --start
Started monitoring of <your_repository>

$ python3 src/main.py
[will print the monitored branches and commits to STDOUT]

```