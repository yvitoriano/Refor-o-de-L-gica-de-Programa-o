num = int(input("Digite um número de 1 a 10 para saber a tabuada: "))

for i in range(0,11,2):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")

#Forma 2

#i = 0 
#while i < 10:
#    print(f"{num} x {i} = {resultado}")
#    i = i + 1

