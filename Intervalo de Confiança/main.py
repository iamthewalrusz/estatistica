import numpy as np
from scipy import stats

arr_custom = np.random.normal(loc=1.65, scale=0.1, size=50) # 
print(arr_custom)
media_amostral = np.mean(arr_custom)
print(media_amostral)

# intervalo = stats.norm.interval()