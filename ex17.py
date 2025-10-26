import math

a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))

# Pesquisei e encontrei essa funcionalidade (math.hypot)
hpt = math.hypot(a,b)

# Se não soubesse dessa funcionalidade, ficaria dessa forma (hpt = ((a**2 + b**2)**1/2)

print (f'A hipotenusa vai medir {hpt:.1f}')