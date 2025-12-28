# programa que leia um valor em metros e o exiba em centimetros e milimetros
v = float(input('Digite um valor em metros: '))
km = v / 1000
hm = v / 100
dam = v / 10
dm = v * 10
cm = v * 100
mm = v * 1000

print(f'{v}m equivale a: \n{km}km \n{hm}hm \n{dam}dam \n{dm}dm \n{cm}cm \n{mm}mm')