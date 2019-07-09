'''f.u.p que calcule o valor de uma coxinha, dado que
o usuario vai pedir mais de uma'''

valor = float(input("Qual o valor da coxinha(R$)? "))
qtd = int(input("Quantas coxinhas voce quer? "))

total = (valor * qtd)
print("Valor total é de R$%.2f" % total)
