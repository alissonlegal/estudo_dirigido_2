'''
Faça um programa que calcule o valor total investido por um colecionador em sua
coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a
quantidade de CDs e o valor para em cada um.
'''

qtdCD = int(input("Digite a quantidade de CD's: "))
cds = []
cont = 1
for cd in range(qtdCD):
    valor = cds.append(float(input("Qual o valor do %.f CD ? " %(cd+1))))
    cont += 1

media = sum(cds) / len(cds)
print("Valor investido e de: R$%.2f " % sum(cds))
print("e o valor medio investido e de: R$%.2f " % media)