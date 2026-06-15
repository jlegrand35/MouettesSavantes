import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# importer jeu de donnees:
df = pd.read_csv("/home/legrand/Documents/Mouettes_Savantes/2024/Rennes_temperatures.csv")


print(df.head()) # affiche les premieres lignes du tableau

plt.scatter(df['Date'], df['Tmin']) # tracer la série temporelle
plt.title('Temperature Minimale')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.show()
