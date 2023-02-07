# Escreva um programa que leia o valor em metros e o exiba convertido em centimetros e milimetros
metros = float(input('Uma distância em metros: '))
km = metros * 1000
hm = metros * 100
dam = metros * 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print('{}m corresponde a: \n{:.0f}km; \n{:.0f}hm; \n{:.0f}dam; \n{:.0f}dm; \n{:.0f}cm; \n{:.0f}mm.'.format(metros, km, hm, dam, dm, cm, mm))
