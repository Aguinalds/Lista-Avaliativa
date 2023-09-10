"""
Estratégia:
- O programa inicia solicitando ao jogador o tamanho do tabuleiro.
- Cria-se um tabuleiro vazio representado por uma lista de listas.
- Os jogadores 'X' e 'O' alternam suas jogadas, inserindo suas marcações nas posições do tabuleiro.
- Após cada jogada, o programa verifica se há um vencedor ou empate usando a função 'check_winner'.
- O jogo continua até que haja um vencedor ou todas as posições estejam preenchidas.

Detalhamento das Estruturas Usadas:
- O tabuleiro é representado como uma lista de listas, onde cada elemento é uma string ('X', 'O' ou espaço em branco).
- A função 'check_winner' verifica se um jogador ganhou verificando linhas, colunas e diagonais do tabuleiro.

Documentação das Funções:
- print_board: Imprime o estado atual do tabuleiro na saída padrão.
- check_winner: Verifica se um jogador ganhou o jogo.
- main: Função principal que executa o jogo da velha.

"""

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (len(board) * 3 - 1))

def check_winner(board, player):
    size = len(board)

    # Verificar linhas e colunas
    for i in range(size):
        if all(board[i][j] == player for j in range(size)) or all(board[j][i] == player for j in range(size)):
            return True

    # Verificar diagonais
    if all(board[i][i] == player for i in range(size)) or all(board[i][size - 1 - i] == player for i in range(size)):
        return True

    return False

def main():
    size = int(input("Digite o tamanho do tabuleiro (NxN): "))
    board = [[" " for _ in range(size)] for _ in range(size)]
    player = "X"
    
    for _ in range(size * size):
        print_board(board)
        row = int(input(f"Jogador {player}, escolha a linha (1-{size}): ")) - 1
        col = int(input(f"Jogador {player}, escolha a coluna (1-{size}): ")) - 1

        if 0 <= row < size and 0 <= col < size and board[row][col] == " ":
            board[row][col] = player
        else:
            print("Posição inválida. Tente novamente.")
            continue

        if check_winner(board, player):
            print_board(board)
            print(f"Jogador {player} venceu! Parabéns!")
            break

        player = "O" if player == "X" else "X"

    else:
        print_board(board)
        print("Empate! O jogo acabou sem vencedor.")

if __name__ == "__main__":
    main()
