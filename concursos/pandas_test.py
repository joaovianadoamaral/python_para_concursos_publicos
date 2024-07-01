import pandas as pd
from IPython.display import display
dados = [['João', 10], ['Júlia', 8.5], ['Andréia', 9]]
df = pd.DataFrame(dados, columns=['Nome', 'Nota'])

print(df)

print()

print(df.head(1))

display(df.T)

print()