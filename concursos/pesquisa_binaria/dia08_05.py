# funcao pesquisa binaria
def pesquisa_binaria(lista_ordenada, int_answer):
    indice_inicio = 0
    indice_fim = len(lista_ordenada) - 1

    while indice_inicio <= indice_fim :
        indice_meio = (indice_inicio + indice_fim) // 2
        if lista_ordenada[indice_meio] == int_answer:
            return indice_meio
        
        if lista_ordenada[indice_meio] < int_answer:
            indice_inicio = indice_meio + 1
        
        if lista_ordenada[indice_meio] > int_answer:
            indice_fim = indice_meio - 1

    return -1

# regra: a lista deve estar ordenada
inicio = 1
fim = 100
lista_ordenada = list(range(inicio, fim + 1))

# entrada usuario
try:
    message = f'Digite um numero entre {inicio} e {fim}: '
    int_answer = int(input(message))

except ValueError:
    while True:
        error_message = f'Algo deu errado... Tente novamente'
        print(error_message)

        message = f'Digite um numero entre {inicio} e {fim}: '
        answer = input ( message )
        if answer.isnumeric():
            int_answer = int ( answer )
            break

posicao_alvo = pesquisa_binaria(lista_ordenada, int_answer)
print('Posição do numero na minha lista: ', posicao_alvo)