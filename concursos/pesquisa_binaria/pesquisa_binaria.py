# fazer a pesquisa binária todos os dias
# regra : a lista deve estar ordenada
inicio = 1
fim = 100
lista_ordenada = list(range(inicio, fim + 1))

# variáveis
indice_inicio = 0
indice_fim = len(lista_ordenada) - 1
indice_meio = (indice_inicio + indice_fim) // 2

# entrada usuário
alvo =  int(input(f'Digite um número entre {inicio} a {fim}: '))

# escreva o programa aqui
while indice_inicio < indice_fim:
    if lista_ordenada[indice_meio] == alvo:
        break

    if lista_ordenada[indice_meio] > alvo:
        indice_fim = indice_meio - 1

    if lista_ordenada[indice_meio] < alvo:
        indice_inicio = indice_meio + 1

    indice_meio = (indice_inicio + indice_fim) // 2

# saída usuário
print('a posição : ', indice_meio)
print('o elemento : ', lista_ordenada[indice_meio])