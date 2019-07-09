'''f.u.p que peca um numero inteiro e determine se ele e ou nao um numero
primo. um numero primo e aquele que e divisivel somente por ele mesmo e por 1
'''

numero = int(input("Digite um número e veja se ele e primo: "))
rest = 0
for c in range(1, numero + 1):
    if numero % c ==0:
        rest = rest + 1
if rest == 2:
    print(numero, "É PRIMO")
else:
    print(numero, "NÃO É PRIMO")
