import os

ALLOWED_COMMANDS = ["ls", "pwd", "whoami", "cat", "echo"]

def is_safe_command(command: str):
    base = command.split(" ")[0]
    return base in ALLOWED_COMMANDS

def run_bash(command: str):
    if not is_safe_command(command):
        return "Comando não permitido por segurança"

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