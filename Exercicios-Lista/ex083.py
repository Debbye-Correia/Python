expressao = str(input('Digite a expressão: '))
pilha = []
for simbolo in expressao:
    if simbolo == '(': # Cada vez que eu abro um parentese abrindo ele vai add na pilha
        pilha.append('(')
    elif simbolo == ')':  # e quando eu coloco um parentese fechando
        if len(pilha) > 0: # ele vai remover um parentese da pilha (encontrando seu par)
            pilha.pop()
        else:
            pilha.append(')') # se a pilha estiver vazia, ele vai add um parentese fechando e dar break
            break             # Significando que a pilha nao esta vazia, e dando o erro
if len(pilha) == 0:  #Vai significar que cada parentese que abriu tbem fechou
    print('Sua expressão está valida!')
else:
    print('Sua expressão está incorreta!')

