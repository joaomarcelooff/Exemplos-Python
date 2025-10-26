print ('=' * 25)
print ('ANALISADOR DE TRIÂNGULOS')
print ('=' * 25)

a = float(input('Insira o valor de lado A: '))
b= float(input('Insira o valor de lado B: '))
c = float(input('Insira o valor de lado C: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    print ('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print ('Os segmentos acima NÃO PODEM FORMAR um triângulo')