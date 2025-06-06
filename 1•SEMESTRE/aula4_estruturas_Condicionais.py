#Verificar qual dos dois números é maior:

# a = int(input("Insira um Nº: "))
# b = int(input("insira outro N°: "))

# if a > b:
#     print(f"o número maior é {a}")
# else:
#     print(f"o numero maior é {b}")

# Escreva um programa que peça ao usuário para digitar sua idade. Se a idade for maior ou igual a 18, o programa deve exibir "Você é maior de idade.

# user_Name = input("Qual seu nome? ")
# print("Ola", user_Name)
# age = int(input ("Qual sua idade? "))

# if age >= 18:
#     print("Você é maior de idade")
# else:
#     print("Você é menor de maior")

 # Escreva um programa que solicite ao usuário um número e, se o número for maior que 0, exiba "Número positivo.".

# numero = float(input("Olá, insira um nº: "))
# if numero >= 0:
#     print("Este numero é positivo")
# else:
#     print("Este numero é negativo")

#Escreva um programa que peça ao usuário para digitar uma senha. Se a senha digitada for "1234", exiba "Acesso permitido.", senão, exiba "Acesso negado.".

# key = int(input("Olá, digite sua senha: "))
# if key == 1234:
#     print("Acesso liberado")
# else: 
#     print("Acesso negado!")

#4. Escreva um programa que peça ao usuário sua idade e exiba: a. "Criança" se for menor que 12 anos / b. "Adolescente" se for entre 12 e 17 anos / c. "Adulto" se for 18 anos ou mais

# age = int(input("Qual sua idade? "))

# if age < 12:
#     print("Criança")
# elif age >=12 and age <=17:
#     print("Adolescente")
# else:
#     print("Adulto")

#5. Peça ao usuário sua idade e exiba o preço do ingresso: a. Menos de 12 anos: R$10,00 / b. Entre 12 e 17 anos: R$15,00 / c. 18 anos ou mais: R$20,00

# age = int(input("Ola, qual sua idade? "))

# if age < 12:
#     print("Valor ingresso R$10,00")
# elif age >= 12 and age <=17:
#     print("Valor ingresso R$15,00")
# else:
#     print("Valor ingresso R$20,00")

#OPERADORES LÓGICOS : AND (E), OR (OU), NOT(NÃO/ NEGAÇÃO)

num =  int(input("Insira um valor: "))

if num >=0 and num <=10:
    print("Numero dentro da faixa")
else:
    print("Numero fora da faixa")
