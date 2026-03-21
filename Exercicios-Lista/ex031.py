# ler distancia de uma viagem em km. calcular preço 0,50 centavos por viagens ate 200km, e 0,45 para viagens maius
# longas
dis = float(input('Qual a distancia da sua viagem? '))
if dis > 200:
    valor = dis * 0.45
else:
    valor = dis * 0.50
print(f'O custo da viagem é de R${valor}')

# FORMA DO IF SIMPLIFICADA
#  valor = dis * 0.50 if dis <=200 else valor = dis * 0.45