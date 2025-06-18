#1)Peça para o usuário 8 números.
#Mostre quantos desses números são maiores que 10

num = []

for i in range(8):
    num.append(int(input("Digite um número: ")))

maiorque10 = 0

for i in range(8):
    if num[i] > 10:
        print(num[i])
        maiorque10 = maiorque10 + 1

print(f"{maiorque10} números são maiores que 10!")
