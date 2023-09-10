"""
Estratégia:
- Usei um dicionário global chamado 'banco_usuarios' para armazenar os usuários.
- Criei uma função 'cadastrar_usuario' para cadastrar um usuário com campos obrigatórios e opcionais.
- Outra função 'imprimir_usuarios' oferece opções para imprimir todos os usuários ou filtrá-los com base em nomes e campos específicos.
- A função principal 'main' exibe um menu para o usuário escolher entre as opções de cadastro, impressão ou encerramento.

Detalhamento das Estruturas:
- Usei dicionários para representar os usuários, onde as chaves são os nomes dos campos e os valores são os dados correspondentes.
- Os campos obrigatórios são definidos pelo usuário em tempo de execução, enquanto os campos opcionais são adicionados conforme o usuário deseja.

Documentação das Funções:
- cadastrar_usuario: Recebe uma lista de campos obrigatórios e permite ao usuário cadastrar um novo usuário. Retorna o dicionário do usuário criado e o armazena em 'banco_usuarios'.
- imprimir_usuarios: Oferece opções para imprimir todos os usuários, filtrar por nomes, campos ou ambos. Aceita argumentos flexíveis para especificar critérios de filtro.
- main: Função principal que exibe o menu e gerencia a interação com o usuário.
"""

# Dicionário global para armazenar os usuários
banco_usuarios = []

# Função para cadastrar um usuário com campos obrigatórios e opcionais
def cadastrar_usuario(campos_obrigatorios):
    usuario = {}

    # Solicitar dados para os campos obrigatórios
    for campo in campos_obrigatorios:
        valor = input(f"Digite o valor para '{campo}': ")
        usuario[campo] = valor

    # Solicitar dados para campos opcionais até que o usuário digite "sair"
    while True:
        campo = input("Digite um campo opcional ou 'sair' para encerrar: ")
        if campo.lower() == 'sair':
            break
        valor = input(f"Digite o valor para '{campo}': ")
        usuario[campo] = valor

    banco_usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

# Função para imprimir usuários com várias opções
def imprimir_usuarios():
    opcao = int(input("1 - Imprimir todos\n2 - Filtrar por nomes\n3 - Filtrar por campos\n4 - Filtrar por nomes e campos\n"))

    if opcao == 1:
        for usuario in banco_usuarios:
            print(usuario)
    elif opcao == 2:
        nomes = input("Digite os nomes separados por vírgula: ").split(",")
        for usuario in banco_usuarios:
            if usuario.get("nome") in nomes:
                print(usuario)
    elif opcao == 3:
        campos = input("Digite os campos separados por vírgula: ").split(",")
        for usuario in banco_usuarios:
            if all(usuario.get(campo) is not None for campo in campos):
                print(usuario)
    elif opcao == 4:
        nomes = input("Digite os nomes separados por vírgula: ").split(",")
        campos = input("Digite os campos separados por vírgula: ").split(",")
        for usuario in banco_usuarios:
            if (usuario.get("nome") in nomes) and (all(usuario.get(campo) is not None for campo in campos)):
                print(usuario)
    else:
        print("Opção inválida.")

# Função principal
def main():
    campos_obrigatorios = input("Digite os nomes dos campos obrigatórios separados por vírgula: ").split(",")
    
    while True:
        print("\nMenu:")
        print("1 - Cadastrar usuário")
        print("2 - Imprimir usuários")
        print("0 - Encerrar")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            cadastrar_usuario(campos_obrigatorios)
        elif escolha == "2":
            imprimir_usuarios()
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
