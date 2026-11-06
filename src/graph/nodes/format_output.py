from src.graph.state import State


def format_output(state: State) -> dict:
    return {"resultado": f"Pergunta: {state['pergunta']}\nResposta: {state['resposta_llm']}"}