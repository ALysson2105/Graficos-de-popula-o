import matplotlib.pyplot as plt

brasil_populacao = [174.5, 176.9, 179.3, 181.8, 184.2, 186.7, 189.1, 191.5, 193.9, 196.3, 198.7, 201.1, 203.5, 205.9, 208.3, 210.7, 213.1, 215.5, 217.9, 220.3, 222.7, 225.1, 227.5]
colombia_populacao = [43.9, 44.7, 45.5, 46.3, 47.1, 47.9, 48.8, 49.6, 50.4, 51.2, 52.0, 52.9, 53.7, 54.5, 55.3, 56.1, 57.0, 57.8, 58.6, 59.4, 60.2, 61.0, 61.8]
argentina_populacao = [37.8, 38.5, 39.2, 39.8, 40.5, 41.2, 41.9, 42.6, 43.3, 43.9, 44.6, 45.3, 46.0, 46.7, 47.4, 48.1, 48.8, 49.4, 50.1, 50.8, 51.5, 52.2, 52.9]

anos = range(2000, 2023)

# Gráfico Treemap
plt.figure(figsize=(8, 6))
plt.title('População por país')
plt.pie([brasil_populacao[-1], colombia_populacao[-1], argentina_populacao[-1]], labels=['Brasil', 'Colômbia', 'Argentina'], autopct='%1.1f%%')
plt.axis('equal')
plt.show()

# Gráfico de Barras
plt.figure(figsize=(10, 6))
plt.title('População por país')
plt.bar(anos, brasil_populacao, width=0.3, align='center', label='Brasil')
plt.bar(anos, colombia_populacao, width=0.3, align='edge', label='Colômbia')
plt.bar(anos, argentina_populacao, width=-0.3, align='edge', label='Argentina')
plt.xlabel('Ano')
plt.ylabel('População (em milhões)')
plt.legend()
plt.show()

# Gráfico de Escala Discreta
plt.figure(figsize=(8, 6))
plt.title('População por país')
plt.scatter(anos, brasil_populacao, marker='o', label='Brasil')
plt.scatter(anos, colombia_populacao, marker='s', label='Colômbia')
plt.scatter(anos, argentina_populacao, marker='^', label='Argentina')
plt.xlabel('Ano')
plt.ylabel('População (em milhões)')
plt.legend()
plt.show()
