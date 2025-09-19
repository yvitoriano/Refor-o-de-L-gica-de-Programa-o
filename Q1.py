idade = int(input("Qual a sua idade? "))

if idade < 16:
    print("Não pode votar")
elif idade == 16 or idade == 17 or idade > 70 :
    print("Voto opcional")
else:
    print("Voto obrigatório")
