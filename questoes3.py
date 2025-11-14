entrada = int(input ('Qual a hora da entrada ?'))
saida = int(input('Qual a hora da saida ?'))


def valida_valores():
    entrada = int(input('Qual a hora de entrada ?')) 
    if entrada > 23 or entrada< 0 
        raise ValueError 
    saida = int(input('Qual a hora da saida ?'))
    if saida > 23 or saida < 0 
        raise ValueError 
    return calcula_estacionamento(entrada, saida )

if entrada > 23: 
def calcula_estacionamento(entrada, saida):
    if entrada > saida:
        print('Você inseriu os parâmetrso incorretamente')
        return 
    if entrada > 23 or entrada < 0 or saida > 23 or saida < 0:
        print('Você inseriu uma hora inválida ')
        return
    diferenca_horario = saida - entrada
    if diferenca_horario <= 2:
        valor = 4 * diferenca_horario
        return valor 
    else:
        valor = 3 * (diferenca_horario-2) + 8
        return valor 
print(calcula_estacionamento(entrada, saida))



