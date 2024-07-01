import numpy as np

# criando um array unidimensional
lista = [1,2,3,4,5,6]
numbers = np.array(lista)

# Um sai com vírgula e o outro só com espaço
print(lista)
print(numbers)

# principal diferença entre array e lista
lista = [1, 'oi', True]
array = np.array(lista)
print(lista)
print(array) # como os tipos são diferente ele transforma tudo para str