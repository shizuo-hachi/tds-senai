#Aluno: André Shizuo Hachiguti de Quadros
#SENAI - TDS TURMA:318
perguntas = ["Telefonou para a vítima?\n", "Esteve no local do crime?\n", "Mora perto da vítima?\n", "Devia para a vítima?\n"]
respostas = []
positivas = 0
inp = ""

for i in range(4):
    inp = input(perguntas[i])
    respostas.append(inp)
    if inp == "sim":
        
        positivas = positivas + 1

print(f"Respostas: {respostas}")
print(f"Positivas: {positivas}")

if positivas == 2:
    print("Suspeito")
elif positivas == 3:
    print("Cúmplice")
elif positivas == 4:
    print("Assassino")
else:
    print("Inocente")
