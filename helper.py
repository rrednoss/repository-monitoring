import os


def cronjob_file():
    return os.path.dirname(os.path.realpath(__file__)) + "/monitoring_cronjob.py"


def monitoring_file():
    return os.path.dirname(os.path.realpath(__file__)) + "/_monitoring.txt"


def recording_file():
    return os.path.dirname(os.path.realpath(__file__)) + "/_records.txt"


def access_mode(file):
    if os.path.exists(file):
        return "r"
    else:
        return "w+"