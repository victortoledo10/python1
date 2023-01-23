
# Imports necesarios
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
#%matplotlib inline
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

#cargamos los datos de entrada
data = pd.read_csv("C:/Users/67740514/projects/Python1/articulos_ml.csv")
#veamos cuantas dimensiones y registros contiene
data.shape

#son 161 registros con 8 columnas. Veamos los primeros registros
data.head()

# Ahora veamos algunas estadísticas de nuestros datos
data.describe()
print(data.describe())

# Visualizamos rápidamente las caraterísticas de entrada
data.drop(['Title','url', 'Elapsed days'],1).hist()
plt.show()
