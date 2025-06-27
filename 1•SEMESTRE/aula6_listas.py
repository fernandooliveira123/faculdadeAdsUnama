#LISTA
# lista =[0,1,2,3,4,5]
compras = ["café","leite","pão"]
# A = [] #lista vazia
# list (range(5))

#acessando elementos
# print(compras[2])

#modificando elementos em uma lista
# compras [0] = "Suco"
# print(compras)

#PERCORRENDO A LISTA 

# for itens in compras:
#     print(itens)

#SABENDO O INDICE DA LISTA
# for i in range(len(compras)):
#     print(compras[i])

# IMPRIMINDO O INDICE E O VALOR DA LISTA: ENUMERATE 
# for i, item in enumerate (compras):
#     print(f"Item {i}: {item}")

# Para uma lista contendo 5 números inteiros, formular um algoritmo que determine o maior 
# elemento desta lista

# numeros = [10,45,20,62]

# maior = numeros[0]
# for numero in numeros:
#     if numero > maior:
#        maior = numero
#        print(maior)

# Leia as notas de uma turma de cinco estudantes e depois imprima as notas que são maiores do que a média da turma

notas = [] # Lista para armazenar as 5 notas

# Lê as 5 notas do usuário
for i in range(5):
    nota = float(input(f"Insira Sua nota {i+1}: "))
    notas.append(nota)
#calcular média
media = sum (notas) / len(notas)
#imprimindo notas acima da média
print(f"Média da turma {media}")
print("Notas acima da média")
for nota in notas:
    if nota > media:
        print(nota)

