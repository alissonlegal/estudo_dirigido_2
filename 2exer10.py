'''
F.U.P. para verificar se o número fornecido pelo usuário é um número Armstrong
ou não. No caso, em um número de Armstrong de três (3) dígitos, a soma dos
cubos de cada dígito é igual ao número em si.
Por exemplo: 153 = 1*1*1 + 5*5*5 + 3*3*3 // 153 é um número Armstrong.
Nota: o número de Armstrong abcd... = an + bn + cn + dn + ...
+++++++++++++++++++++++++++++++++++++++++++++++++++
'''

numero = int(input("Digite um numero: "))
soma = 0

tempo = numero
while tempo > 0:
   digito = tempo % 10
   soma += digito ** 3
   tempo //= 10

if numero == soma:
   print(numero,"é um número Armstrong")
else:
   print(numero,"não é um número Armstrong")
