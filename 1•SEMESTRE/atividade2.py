# Aluno: Fernando Augusto 
#Matrícula:04183227
#Curso ADS: Manhã
#turma: A

# 2. Crie um programa que solicite dois números ao usuário, some-os e exiba o resultado.

# numero1 = float(input("Insira um numero"))
# numero2 =float(input("Insira mais um numero"))
# resultado = numero1 + numero2
# print("Seu numero 1 com o numero 2 somados gera o resultado", resultado)

# 4. Escreva um programa que leia um número e exiba o seu dobro e triplo

# numero = int(input("Me mande um numero =D"))
# dobro = numero * 2
# triplo = numero * 3
# print ("o dobro do numero é:", dobro)
# print ("o dobro do numero é:", triplo)

# # 5. Crie um programa que peça a idade do usuário e exiba quantos dias ele já viveu (considerando que um ano tem 365 dias)

# idade = int(input("Olá qual a sua idade?"))
# diasVividos = idade * 365
# print("Você já viveu aproximadamente:", diasVividos,  "dias, parabéns que venham muitas mais dias de vida!")

#IMC EM  PYTHON
peso = float(input("Qual seu peso em kg? "))
estatura = float(input("Qual sua altura em cm? "))

# Converter altura de cm para metros
converterAltura_metros = estatura / 100

# Calcular IMC
resultadoImc = peso / (converterAltura_metros ** 2)

print("Seu IMC é:", round(resultadoImc, 2))

# Classificação do IMC
if resultadoImc < 18.5:
    print("Classificação: Baixo peso")
elif 18.5 <= resultadoImc < 24.9:
    print("Classificação: Peso saudável")
elif 25 <= resultadoImc < 29.9:
    print("Classificação: Sobrepeso")
elif 30 <= resultadoImc < 34.9:
    print("Classificação: Obesidade nível 1")
elif 35 <= resultadoImc < 39.9:
    print("Classificação: Obesidade nível 2")
else:
    print("Classificação: Obesidade mórbida")
