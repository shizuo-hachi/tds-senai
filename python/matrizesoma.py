#3) Peça ao usuário para digitar 4 números. 
# Coloque esses números numa matriz 2x2 e mostre a matriz e a soma

matriz = []
soma = 0

for i in range(2):
    linha = []
    for j in range(2):
        numero = int(input(f"Digite o número para a posição [{i}][{j}]: "))
        linha.append(numero)
        soma += numero
    matriz.append(linha)

print("\nMatriz 2x2:")
for linha in matriz:
    print(linha)

print(f"\nSoma dos elementos da matriz: {soma}")
