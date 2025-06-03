#Crie um programa realize uma contagem regressiva em tela, começando em 10 até 1 e no final exiba a mensagem “FIM!”

# for i in range(10,0,-1):
#     print(i)
# print("FIM")

#Crie um programa que receba 10 notas de alunos e calcule a média aritmética delas

soma = 0 
for i in range(1,11):
    nota = float(input("Insira sua nota: "))
    soma += nota 
media = soma / 10
print (f"sua média é, {media}")

