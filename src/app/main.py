from src.graph.builder import build_graph


OPCOES = {
    "1": "frota",
   "2": "xadrez"
}

def main() -> None:
    graph = build_graph()

    while True:
        print('\nSobre o que deseja falar?')
        print('1 - Frota de navios')
        print('2 - Peças de xadrez')
        print('0 - SAIR')
        opcao = input('Escolha:').strip()

        if opcao == '0':
            print('Até mais')
            break
        if opcao not in OPCOES:
            print('Opção inválida. Escolha 1, 2 ou 0.')
            continue
        pergunta = input("Pergunta: ").strip()
        if not pergunta:
            print("Digite uma pergunta.")
            continue

        saida = graph.invoke({"assunto": OPCOES[opcao], "pergunta": pergunta})
        print()
        print(saida["resultado"])

if __name__ == "__main__":
    main()