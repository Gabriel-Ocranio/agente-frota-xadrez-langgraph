import json

from src.graph.prompt.prompt import PROMPT_FROTA, PROMPT_XADREZ
from src.graph.state import State
from src.utils.llm_adapter import get_llm

PROMPTS = {
    "frota": PROMPT_FROTA,
    "xadrez": PROMPT_XADREZ
}

def decide(state: State) -> dict:
    prompt = PROMPTS[state["assunto"]]
    chain = prompt | get_llm()
    resposta = chain.invoke(
        {
            "pergunta": state["pergunta"],
            "frota": json.dumps(state["frota"], ensure_ascii=False),
            "xadrez": json.dumps(state["xadrez"], ensure_ascii=False),
        }
    )
    return {"resposta_llm": resposta.content}