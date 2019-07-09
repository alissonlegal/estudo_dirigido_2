'''f.u.p que calcule o tempo de utilizacao de um patinete eletrico, voce,
deve saber
que existe uma taxa de utilizacao que permite ao usuario utilizar o patinete
por 10 minutos que e de R$5,00. passando disso, o preco e acrescido de 20%
ao final da utilizacao deve ser mostrado ao usuario o quanto deve pagar pela
utilizacao
'''

tempoUsado = int(input("Qual o tempo usado em minutos? "))
totalPagar = 0


if tempoUsado <= 10:
    totalPagar = 5
    print("Total a pagar: R$%.2f " % totalPagar)
else:
    tempoAcres = tempoUsado - 10
    totalPagar = 5 + (tempoAcres * (5*0.2))
    print("Total a pagar: R$%.2f " % totalPagar)

'''
preco = 5
tempo_excedente = 0
tempo_minutos = int(input("Tempo utilizado: "))
if tempo_minutos <= 10:
    print("Valor a ser paga: ", preco)
else: 
    tempo_minutos > 10
    tempo_excedente = (tempo_minutos - 10)
    preco = 5 + (tempo_excedente * 5 * 0.2)
    print("Valor a ser pago: ", preco)
'''