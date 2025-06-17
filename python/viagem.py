dist = float(input("Digite a distância em km: "))
consumo = float(input("Qual o consumo do carro em km/l? "))
precogas = float(input("Qual o preço da gasolina? "))
litros = 0.0
dinheiros = 0.0

litros = dist/consumo
dinheiros = precogas * litros

print(f"Serão necessários {litros}l para fazer a viagem")
print(f"A viagem vai custar R${dinheiros}")
