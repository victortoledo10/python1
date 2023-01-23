import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


#Ejemplo 3 https://naps.com.mx/blog/3-ejemplos-explicados-de-machine-learning-en-python/

ventas = pd.read_csv("C:/Users/67740514/projects/Python1/ventas2.csv")
objetivo = "monto"
independientes = ventas.drop(columns=['monto']).columns


modelo = LinearRegression()
modelo.fit(X=ventas[independientes], y=ventas[objetivo])

ventas["ventas_prediccion"] = modelo.predict(ventas[independientes])
preds = ventas[["monto", "ventas_prediccion"]].head(50)

print (ventas[["monto", "ventas_prediccion"]].head(50))


talvez = modelo.predict([[41,1,1,1]])
print ("Tal vez compre: ")
print (talvez)


preds.plot(kind='bar',figsize=(18,8))
plt.grid(linewidth='2')
plt.grid(linewidth='2')
plt.grid(None)
plt.show()

