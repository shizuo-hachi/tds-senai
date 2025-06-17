nome = ""

while nome != "fim":
    nome = input("Digite o seu nome: ")
    
    if nome == "fim":
        print("Adeus")
        break

    idade = int(input("Digite a sua idade: "))
    if idade >= 18:
        print(f"Parabéns, {nome}! Você pode entrar no churrasco da Yndia!")
    else:
        print(f"Puxa {nome}, que pena! Você é menor de idade... Não pode entrar na festa...")


