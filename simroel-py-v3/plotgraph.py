import pandas as pd
import matplotlib.pyplot as plt

# 1. Ler o arquivo CSV
file_path = "/home/backu/PycharmProjects/simroelfix/simroel-py-v3/Result/new_FF_est2.csv"
data = pd.read_csv(file_path)

# 2. Exibir as primeiras linhas para entender a estrutura dos dados
print(data.head())

# 3. Calcular o número de conexões bloqueadas e a probabilidade de bloqueio
data['Blocked_Connections'] = data['Load'] - data['Allocted']
data['Blocking_Probability'] = data['Blocked_Connections'] / data['Load']

# 4. Agrupar por 'Load' e calcular a média da probabilidade de bloqueio
blocking_probability = data.groupby('Load')['Blocking_Probability'].mean()

# 5. Gerar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(blocking_probability.index, blocking_probability.values, marker='o', linestyle='-', color='r', label='Probabilidade de Bloqueio')

# 6. Adicionar título e rótulos
plt.title("Probabilidade de Bloqueio por Carga")
plt.xlabel("Carga (Load)")
plt.ylabel("Probabilidade de Bloqueio")
plt.legend()

# 7. Mostrar o gráfico
plt.grid(True)
plt.show()