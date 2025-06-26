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

numeros = [10,45,20,62]

maior = numeros[0]
for numero in numeros:
    if numero > maior:
       maior = numero
       print(maior)