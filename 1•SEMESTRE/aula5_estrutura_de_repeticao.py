#Crie um programa realize uma contagem regressiva em tela, começando em 10 até 1 e no final exiba a mensagem “FIM!”

# for i in range(10,0,-1):
#     print(i)
# print("FIM")

#Crie um programa que receba 10 notas de alunos e calcule a média aritmética delas

# soma = 0 
# for i in range(1,11):
#     nota = float(input("Insira sua nota: "))
#     soma += nota 
# media = soma / 10
# print (f"sua média é, {media}")

#teste computador
##teste tablet()

# soma = 0 
# for i in range(1,11):
#     nota = float(input("Insira sua nota: "))
#     soma += nota 
# media = soma / 10
# print (f"sua média é, {media}")

#Crie um programa de calculadora, 
# onde o usuário informa dois números e uma opção de cálculo:a. 1 - Soma; 2 - Subtração; 3 - Divisão; 4 - Multiplicação


print("Calculadora básica em Python")
print("Escolha a operação:")
print("1- Soma")
print("2-Subtracao")
print("3 - Multiplicacao")
print("4- Divisao")

opcao = int((input("Digite a opcao de 1 a 4: ")))
num1  = float((input("Insira um valor: ")))
num2  = float(input("Insira o segundo valor: "))

if opcao == 1 :
    resultado = num1 + num2
    print(resultado)
elif opcao == 2:
    resultado = num1 - num2
    print(resultado)
elif opcao == 3:
    resultado = num1 * num2
    print(resultado)
elif opcao == 4:
    resultado = num1 / num2
    print(resultado)
else:
    print("Erro: divisao por 0")

