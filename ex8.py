m = float(input('Insira um valor em metros que será convertido para as demais medidas: '))

km = m  / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print (f'{m:.0f}m equivale à \n {km}km \n {hm}hm \n {dam}dam \n {dm:.0f}dm \n {cm:.0f}cm \n {mm:.0f}mm')
