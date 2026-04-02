import json
import re

def extract_json(text):
    try:
        return json.loads(text)
    except:
        pass

    # tenta extrair JSON do meio do texto
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except:
            pass

    return {
        "action": "none",
        "input": ""
    }