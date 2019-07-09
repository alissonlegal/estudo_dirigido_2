'''
F.U.P. que, dado um conjunto de N números, determine o menor valor, o maior
valor e a soma dos valores. Faça com que ele aceite apenas números entre 0 e
1000.
'''

lista = []
count = 0

quant = int(input("Digite a quantiade de número que deseja digitar: "))
while quant != count:
    numero = float(input("Digite um número: (entre 0 e 1000) "))

    while numero > 1000 or numero < 0:
        numero = float(input("Digite um número[erro]: "))

    lista.append(numero)
    count += 1

print("Lista: ", lista, "\nMaior: ", max(lista), "\nMenor: ", min(lista))
print("Soma: ", max(lista) + min(lista))