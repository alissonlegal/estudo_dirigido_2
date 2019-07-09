'''
F.U.P. para imprimir todo o número primo em um intervalo.
'''

numero = int(input("\nDigite um número: "))
lista = []
divisoes = 0

for i in range(numero + 1):
    if i % 2 == 1 and i != 2:
        lista.append(i)
        divisoes += 1
    else:
        divisoes += 1
print("Números primos: ", lista)
