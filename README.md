# Agente Frota e Xadrez com LangGraph

Agente em Python que responde perguntas sobre uma frota de navios e sobre peças de xadrez. O usuário escolhe o assunto em um menu, e o agente usa o prompt e os dados correspondentes.

## Funcionalidades

- Menu para escolher entre frota de navios e peças de xadrez
- Perguntas livres em português
- Prompts especializados para cada assunto
- Dados guardados em arquivos JSON
- Grafo LangGraph com 3 nós em sequência
- Modelo configurado pelo arquivo `.env`

## Como funciona

```text
main.py → receive → decide → format_output → resposta na tela
```

| Etapa | Função |
|---|---|
| `main.py` | Mostra o menu e recebe a pergunta |
| `receive` | Lê os arquivos JSON |
| `decide` | Escolhe o prompt pelo assunto e chama o modelo |
| `format_output` | Monta o texto final |

## Estrutura do projeto

```text
.
├── data/
│   ├── frota_simples.json
│   └── xadrez_pecas.json
├── src/
│   ├── app/
│   │   └── main.py
│   ├── graph/
│   │   ├── nodes/
│   │   │   ├── decide.py
│   │   │   ├── format_output.py
│   │   │   └── receive.py
│   │   ├── prompt/
│   │   │   └── prompt.py
│   │   ├── builder.py
│   │   └── state.py
│   └── utils/
│       └── llm_adapter.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Tecnologias

- Python 3.13
- LangGraph
- LangChain
- Groq

## Como executar

Os comandos abaixo são para o cmd do Windows.

1. Clone o repositório e entre na pasta:

```cmd
git clone https://github.com/SEU-USUARIO/agente-frota-xadrez-langgraph.git
cd agente-frota-xadrez-langgraph
```

2. Crie e ative o ambiente virtual:

```cmd
python -m venv .venv
.venv\Scripts\activate
```

3. Instale as dependências:

```cmd
pip install -r requirements.txt
```

4. Copie o arquivo de exemplo:

```cmd
copy .env.example .env
```

5. Abra o `.env` e preencha sua chave do Groq:

```env
LLM_PROVIDER=groq
LLM_MODEL=openai/gpt-oss-20b
GROQ_API_KEY=sua-chave-aqui
```

6. Execute o programa pela raiz do projeto:

```cmd
python -m src.app.main
```

## Exemplos de perguntas

**Frota de navios**

- Qual navio chega primeiro?
- Qual navio percorre a maior distância?

**Peças de xadrez**

- Como o cavalo se move?
- O peão pode capturar para frente?

## Limitações

As contas e respostas são geradas pelo modelo e não passam por validação no código. Por isso, ele pode errar um cálculo ou nem sempre seguir as instruções do prompt.
