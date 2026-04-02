from parser import extract_json
from memory import add_memory, search_memory
from langchain_community.llms import Ollama
from config import MODEL
from tools import run_bash, read_file
import json

llm = Ollama(model=MODEL)

def planner(user_input):
    memory_context = search_memory(user_input)

    prompt = f"""
        Você é um sistema de decisão de ações.

        REGRAS OBRIGATÓRIAS:
        - Você NÃO responde o usuário
        - Você APENAS decide uma ação
        - Você DEVE usar JSON válido
        - Se a pergunta envolver sistema, arquivos ou comandos → use "bash"

        Memória:
        {memory_context}

        Entrada:
        {user_input}

        Responda SOMENTE com JSON:

        {{
        "action": "bash | read_file | none",
        "input": "comando ou argumento"
        }}
    """
    raw = llm.invoke(prompt)
    return extract_json(raw)

def executor(plan):
    action = plan.get("action")
    action_input = plan.get("input", "")

    if action == "bash":
        return run_bash(action_input)

    elif action == "read_file":
        return read_file(action_input)

    return "Nenhuma ação executada"

def responder(user_input, result):
    prompt = f"""
        Usuário: {user_input}

        Resultado da ação:
        {result}

        Responda de forma clara e útil para o usuário.
    """
    return llm.invoke(prompt)

def run():
    while True:
        user_input = input(">> ")

        plan = planner(user_input)

        result = executor(plan)

        response = responder(user_input, result)

        print("\n🤖", response)

        add_memory({
            "input": user_input,
            "plan": plan,
            "result": result
        })

if __name__ == "__main__":
    run()