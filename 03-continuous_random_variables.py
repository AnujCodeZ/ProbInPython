import numpy as np 
import matplotlib.pyplot as plt 
from scipy import stats

# Uniform distributions
print(np.random.uniform(low=-2, high=2))

sample = np.random.uniform(low=-2, high=2, size=10000)
plt.hist(sample, density=True)
plt.show()

# In scipy
X = stats.uniform(-2, 4)
print(X.pdf(1.2))