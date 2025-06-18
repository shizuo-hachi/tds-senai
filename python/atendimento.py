#2)Crie uma fila para simular o atendimento de pessoas 
# (primeiro que entra, primeiro que sai)
fila = []

def adicionar_pessoa(nome):
    fila.append(nome)
    print(f"{nome} foi adicionado à fila.")

def atender_pessoa():
    if fila:
        nome = fila.pop(0)
        print(f"{nome} foi atendido.")
    else:
        print("Não há ninguém na fila.")
def mostrar_fila():
    if fila:
        print("Fila de espera:")
        for i, nome in enumerate(fila, start=1):
            print(f"{i}. {nome}")
    else:
        print("A fila está vazia.")

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar pessoa à fila")
        print("2. Atender pessoa")
        print("3. Mostrar fila")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Digite o nome da pessoa: ")
            adicionar_pessoa(nome)
        elif escolha == '2':
            atender_pessoa()
        elif escolha == '3':
            mostrar_fila()
        elif escolha == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()