import json
from config import MEMORY_FILE

MAX_MEMORY = 20

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

    # limita tamanho
    if len(memory) > MAX_MEMORY:
        memory = memory[-MAX_MEMORY:]

    save_memory(memory)

def search_memory(query):
    memory = load_memory()

    # busca simples por relevância
    results = []
    for m in memory:
        if query.lower() in str(m).lower():
            results.append(m)

    return results[-5:]