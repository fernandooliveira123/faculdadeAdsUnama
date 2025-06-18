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
for i, item in enumerate (compras):
    print(f"Item {i}: {item}")
    