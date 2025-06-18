#crie uma pilha para simular uma pilha de livros
# (último que entra, primeiro que sai)

pilha = []
def adicionar_livro(titulo):
    pilha.append(titulo)
    print(f"{titulo} foi adicionado à pilha.")

def remover_livro():
    if pilha:
        titulo = pilha.pop()
        print(f"{titulo} foi removido da pilha.")
    else:
        print("Não há livros na pilha.")

def mostrar_pilha():
    if pilha:
        print("Pilha de livros:")
        for i, titulo in enumerate(reversed(pilha), start=1):
            print(f"{i}. {titulo}")
    else:
        print("A pilha está vazia.")

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar livro à pilha")
        print("2. Remover livro da pilha")
        print("3. Mostrar pilha")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            titulo = input("Digite o título do livro: ")
            adicionar_livro(titulo)
        elif escolha == '2':
            remover_livro()
        elif escolha == '3':
            mostrar_pilha()
        elif escolha == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()