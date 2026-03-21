# ler a velocidade do carro, mais de 80km/h dizer que ele foi multado no valorde de 7 reais por cada km acima do limite
vel = float(input('Qual é a sua velocidade em Km/h? '))
if vel <= 80:
    print('Você esta dentro da margem de velocidade permitida!')
else:
    mul = (vel - 80) * 7
    print(f'Você esta acima da velocidade permitida e foi multado no valor de de R${mul}!')