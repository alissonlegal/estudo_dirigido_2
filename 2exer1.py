'''faca um programa em python que aceite o raio de um circulo do usuario
e calcule a area'''

import math

raio = int(input("Digite o raio do circulo em metros: "))

area = (math.pi * math.pow(raio, 2))

print("A area do circulo e: %.2f m²" % area)
