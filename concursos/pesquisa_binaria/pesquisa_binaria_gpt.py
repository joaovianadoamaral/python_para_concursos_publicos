lista_ordenada = list(range(1, 101))
indice_inicio = 0
indice_fim = len(lista_ordenada) - 1  # Ajuste para o último índice da lista
alvo = int(input('Digite um número entre 1 a 100: '))

while indice_inicio <= indice_fim:  # Condição de parada quando os índices se cruzam
    indice_meio = (indice_inicio + indice_fim) // 2
    
    if lista_ordenada[indice_meio] == alvo:
        print(f'O alvo {alvo} foi encontrado no índice {indice_meio}.')
        break
    elif lista_ordenada[indice_meio] < alvo:
        indice_inicio = indice_meio + 1  # Atualiza o índice de início para a direita do meio
    else:
        indice_fim = indice_meio - 1  # Atualiza o índice de fim para a esquerda do meio
else:
    print(f'O alvo {alvo} não foi encontrado na lista.')