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

# num =  int(input("Insira um valor: "))

# if num >=0 and num <=10:
#     print("Numero dentro da faixa")
# else:
#     print("Numero fora da faixa")

# num = int(input("insira um valor: "))
# if num < 0 or num >10:
#     print("Numero fora da faixa")
# else:
#     print("Numero dentro da faixa")

#OPERADOR NOT (NÃO)

# num = int(input("Insira um número: "))

# if not num >= 30:
#     print("Numero é menor do que 30")

# 6. Escreva um programa que peça ao usuário um ano  e determine se ele é bissexto.
# a. Um ano é bissexto se for divisível por 4, mas não por 
# 100, a menos que seja divisível por 400.

# ano = int(input(" insira um ano: "))

# if (ano % 4 == 0 and ano %100 !=0) or (ano %100 ==0):
#     print(f"o ano {ano} é bisexfo")
# else:
#     print(f"nao {ano} e bisexto")

# 7. Peça ao usuário que digite sua idade e se tem um 
# ingresso VIP (S ou N). A entrada é permitida se:
# a. A idade for maior ou igual a 18 ou se o usuário tiver um 
# ingresso VIP.

# user_age = int(input("insira sua idade: "))
# vip = input("vip? S ou N ?: ")

# if user_age  >= 18 or vip == "S":
#     print("Entrada permitida")
# else:
#     print("Entrada nao permitida")

# 8. Crie um programa que simule um login. O
# sistema deve pedir um nome de usuário e uma
# senha.
# a. O login é permitido se o usuário for "admin" e a
# senha for "1234", ou se o usuário for "convidado" e
# a senha for "guest".
# b. Caso contrário, exiba "Acesso negado"

# username = input("Qual seu usuário: ")
# key_login = input("Qual sua senha?: ")

# if username == "adm" and key_login == 1234:
#     print("Acesso liberado")

# elif username ==  "convidado" and key_login == "guest":
#     print("Acesso liberado")
# else:
#     print("Acesso negado!")
#-----------COM FOR---------------------------------------------- 

# username = input("Qual seu usuário: ")
# key_login = input("Qual sua senha?: ")

# if username == "adm" or username == "convidado" and key_login == 1234 or key_login == "guest":
#     print(f"{username} ACESSO LIBERADO!")
# else:
#     print(f"{username} seu foi Acesso negado")

#---------------------------------------------------------------
# 9. Um mercado oferece descontos de acordo com a quantidade de produtos comprados:
    # a. Se comprar 10 ou mais itens e o total for maior que R$
    # 100,00, o desconto é de 15%.
    # b. Se comprar pelo menos 5 itens ou o total for maior que R$
    # 50,00, o desconto é de 10%.
    # c. Caso contrário, não há desconto.
# Peça ao usuário a quantidade de itens e o valor total da
# compra e informe o valor final com desconto aplicado.

qtd_itens = int(input("Qual a quantidade de items você adquiriu? "))
valor_total = float(input("Qual valor da sua compra? "))

if qtd_itens >= 10 and valor_total >= 100:
    print("Seu desconto é de 15%")
elif qtd_itens >= 5 or valor_total >= 50:
    print("Seu desconto é de 10%")
else:
    print("Não há descontos")
