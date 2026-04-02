import json
from config import MEMORY_FILE

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def add_memory(entry):
    memory = load_memory()
    memory.append(entry)
    save_memory(memory)