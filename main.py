from langchain_community.llms import Ollama
from config import MODEL
from tools import run_bash, read_file
from memory import load_memory, add_memory
import json

llm = Ollama(model=MODEL)

def planner(user_input, memory):
    prompt = f"""
Você é um assistente que decide ações.

Memória:
{memory}

Pergunta:
{user_input}

Responda em JSON:
{{
  "action": "bash | read_file | none",
  "input": "string"
}}
"""
    return llm.invoke(prompt)

def executor(action, action_input):
    if action == "bash":
        return run_bash(action_input)
    elif action == "read_file":
        return read_file(action_input)
    return "Nenhuma ação executada"

def responder(user_input, result):
    prompt = f"""
Usuário: {user_input}
Resultado da ação: {result}

Responda de forma clara.
"""
    return llm.invoke(prompt)

def run():
    while True:
        user_input = input(">> ")

        memory = load_memory()

        plan_raw = planner(user_input, memory)

        try:
            plan = json.loads(plan_raw)
        except:
            print("Erro no planner:", plan_raw)
            continue

        result = executor(plan["action"], plan["input"])

        response = responder(user_input, result)

        print(response)

        add_memory({
            "input": user_input,
            "action": plan,
            "result": result
        })

if __name__ == "__main__":
    run()