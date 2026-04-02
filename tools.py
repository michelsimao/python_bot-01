import os

def run_bash(command: str):
    try:
        return os.popen(command).read()
    except Exception as e:
        return str(e)

def read_file(path: str):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        return str(e)