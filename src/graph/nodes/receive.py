import json
from pathlib import Path

from src.graph.state import State

PASTA_DATA = Path(__file__).resolve().parents[3] / "data" 


def ler_json(nome_arquivo: str) -> dict:
    caminho = PASTA_DATA / nome_arquivo
    return json.loads(caminho.read_text(encoding="utf-8"))


def receive(state: State) -> dict:
    
    return {"frota": ler_json('frota_simples.json'),
            "xadrez": ler_json('xadrez_pecas.json')}