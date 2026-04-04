n = int(input('Digite quantos elementos da Sequencia de Fibonacci você quer ver: '))
fi = 0
seg = 1
while n != 0:
    print(f'[{fi}] [{seg}]', end=' ')
    fi += seg
    seg += fi
    n -= 1
