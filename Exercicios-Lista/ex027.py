# ler o nome completo de uma pessoa e mostrar o primeiro e ultimo nome separadamente
nome = str(input('Digite um nome completo: '))
pri = nome.split()
ult = nome.split().reverse()
print(f'O primeiro nome é: {pri[0]}')
print(f'O ultimo nome é: {ult}')
#nao consegui inverter a ordem da string na lista, para pegar o ultimo nome