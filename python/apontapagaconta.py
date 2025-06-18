conta = float(input("Quanto deu? "))
pagantes = float(input("Quantas pontas? "))

divisao = conta // pagantes
sobra = conta % pagantes

print(f"deu {conta}")
print(f"arredondado: {divisao}")
print(f"sobrou: {sobra}")