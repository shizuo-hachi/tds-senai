nome = ""
while not("fim" == nome):
    nome = input("Escreva seu nome: ")
    idade = int(input("Escreva sua idade: "))
    if idade >= 18:
        print("Pode tirar CNH")
    else:
        print("Não pode tirar CNH, precisa de mais,", 18 - idade, "anos pra isso")
