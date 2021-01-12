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

# Correlated random variables
var1 = 1
var2 = 1
cov = 0.9
cov_matrix = [[var1, cov],
              [cov, var2]]

data = np.random.multivariate_normal([0, 0], cov_matrix, size=1000)

plt.scatter(data[:, 0], data[:, 1])
plt.show()

N = 1000
x = np.random.normal(size=N)
eps = np.random.normal(size=N)
y = x + 0.5 * eps

plt.scatter(x, y)
plt.show()