'''f.u.p para imprimir todos os numeros impares da lista fornecida usando
loop, for e range
'''

numeroi = int(input("Digite o primeiro numero da lista: "))
numerof = int(input("Digite o ultimo numero da lista: "))
# numerof = numerof + 1

print("Numeros impares da lista sao :")
for n in range (numeroi, numerof + 1):
    if n % 2 != 0:
        print(n)
