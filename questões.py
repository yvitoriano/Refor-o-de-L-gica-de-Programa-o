# A = 10 
# B = 20

# C = B  

# B = A 
# A = C

# C = B 

# print(A)
# print(B)
 
# usuario_1 = "José"
# usuario_2 = "Maria"

# print("Usuário 1: ", usuario_1)
# print("Usuário 2: ", usuario_2)

# troca_usuario = usuario_1
# usuario_1 = usuario_2
# usuario_2 = troca_usuario

# print("Usuário 1: ", usuario_1)
# print("Usuário 2: ", usuario_2)



# def valores (valor):

#     if valor > 0:
#         print(f"{valor} é positivo")
#     elif valor < 0:
#         print(f"{valor} é negativo")
#     elif valor == 0:
#         print(f" {valor} é nulo")
#     else:
#         print(f"{valor} é inválido")
    
# print(valores('y'))

def calcular_custo(custo_fabrica):
    distribuidor = custo_fabrica*0.28
    imposto_geral = custo_fabrica*0.45
    custo_total = custo_fabrica + distribuidor + imposto_geral
    return custo_total
print(calcular_custo(10000))
