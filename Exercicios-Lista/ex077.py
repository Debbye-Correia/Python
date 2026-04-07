palavras = ('aprender', 'programar', 'linguagem', 'python','curso','gratis','estudar',
            'praticar', 'trabalhar', 'mercado', 'programador','futuro')
vogal = ('a','e','i','o','u')
for p in palavras:
    print(f'Na palavra {p.upper()} temos:', end=' ')
    for v in vogal:
        if vogal[v] == len(palavras[p]):
            print(vogal[v])



