import pandas as pd
import numpy  as np
import math
from scipy import stats
#import Matplotlib as m

print(pd.__version__)


dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }


brics = pd.DataFrame(dict)


print(brics)

#MEDIA
Velocidad = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
x = np.mean(Velocidad)
print(x)

#MEDIANA
x = np.median(Velocidad)
print(x)

