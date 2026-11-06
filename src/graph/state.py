from typing import TypedDict


class State(TypedDict, total=False):
    pergunta: str
    frota: dict
    xadrez: dict
    resposta_llm: str
    assunto: str
    resultado: str