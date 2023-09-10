"""
Estratégia:
- O jogo lê uma palavra aleatória do arquivo 'lista_palavras.txt' usando a função 'escolher_palavra'.
- O jogador tem um número limitado de tentativas para adivinhar a palavra.
- O jogo usa listas para acompanhar as letras descobertas e as letras já tentadas.
- O jogador fornece uma letra como palpite, e o jogo verifica se a letra está na palavra.
- O jogo exibe o progresso do jogador após cada palpite.

Detalhamento das Estruturas Usadas:
- Listas são usadas para representar as letras descobertas e as letras já tentadas.
- Um arquivo de texto chamado 'lista_palavras.txt' contém uma lista de palavras, uma por linha.
- A função 'random.choice' é usada para escolher uma palavra aleatória do arquivo.

Documentação das Funções:
- escolher_palavra: Lê um arquivo de palavras e escolhe uma palavra aleatória.
- jogar_adivinhacao: Função principal que implementa o jogo de adivinhação de palavras.

"""
import random

def escolher_palavra():
    with open("lista_palavras.txt", "r") as arquivo:
        palavras = arquivo.readlines()
    return random.choice(palavras).strip().lower()

def jogar_adivinhacao():
    palavra = escolher_palavra()
    letras_descobertas = ["_"] * len(palavra)
    letras_tentadas = []

    tentativas = 6

    print("Bem-vindo ao Jogo da Adivinhação de Palavras!")
    print(f"A palavra tem {len(palavra)} letras.")

    while tentativas > 0:
        print("\nPalavra: " + " ".join(letras_descobertas))
        print("Letras tentadas: " + ", ".join(letras_tentadas))
        print(f"Tentativas restantes: {tentativas}")

        tentativa = input("Digite uma letra: ").strip().lower()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite uma única letra válida.")
            continue

        if tentativa in letras_tentadas:
            print("Você já tentou esta letra antes.")
            continue

        letras_tentadas.append(tentativa)

        if tentativa in palavra:
            for i in range(len(palavra)):
                if palavra[i] == tentativa:
                    letras_descobertas[i] = tentativaa
        else:
            tentativas -= 1

        if "_" not in letras_descobertas:
            print("\nParabéns! Você adivinhou a palavra: " + palavra)
            break

    if "_" in letras_descobertas:
        print("\nVocê perdeu! A palavra era: " + palavra)

if __name__ == "__main__":
    jogar_adivinhacao()
