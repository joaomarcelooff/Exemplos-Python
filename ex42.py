print('=' * 25)
print('ANALISADOR DE TRIÂNGULOS')
print('=' * 25)

a = float(input('Insira o valor de lado A: '))
b = float(input('Insira o valor de lado B: '))
c = float(input('Insira o valor de lado C: '))

# Verifica se os lados podem formar um triângulo
if (a + b > c) and (a + c > b) and (b + c > a):
    print('Os segmentos acima PODEM FORMAR um triângulo.')

    # Verifica o tipo de triângulo
    if a == b == c:
        print('Tipo: Triângulo EQUILÁTERO')
    elif a == b or a == c or b == c:
        print('Tipo: Triângulo ISÓSCELES')
    else:
        print('Tipo: Triângulo ESCALENO')

else:
    print ('Os segmentos acima NÃO PODEM FORMAR um triângulo.')