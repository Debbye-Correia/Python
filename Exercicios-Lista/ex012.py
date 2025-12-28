#ler o preço de um produto e mostrar o novo preço com 5% de desconto
p = float(input('Qual é o preço do produto? R$'))
d = p - (p*0.05)
print(f'O valor final deste produto com 5% de desconto é de R${d:.2f}')
# o calculo de porcentagem tambem poderia ter sido da seguinte forma:
# d = p - (p * 5/100)