import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Generating descrete random variables
print(np.random.choice([1, 2, 3], p=[0.2, 0.5, 0.3]))

def count_frequencies(data, relative=False):
    counter = {}
    for element in data:
        if element not in counter:
            counter[element] = 1
        else:
            counter[element] += 1
            
    if relative:
        for element in counter:
            counter[element] /= len(data)
            
    return counter

print(count_frequencies([1, 1, 2, 1]))
print(count_frequencies([1, 1, 2, 1], relative=True))

sample = [np.random.choice([1, 2, 3], p=[0.2, 0.5, 0.3]) for _ in range(10000)]

print(count_frequencies(sample, relative=True))

# Visualizing
freqs = count_frequencies(sample, relative=True)

plt.bar(freqs.keys(), freqs.values())
plt.show()

# Common distributions
# Binomial distributions
binomial_sample = np.random.binomial(10, 0.3, size=100)
print(count_frequencies(binomial_sample, relative=True))

# In scipy
binomial_x = stats.binom(10, 0.3)
print(binomial_x.pmf(1))

x = np.arange(0, 10, 0.5)
plt.plot(x, binomial_x.pmf(x), 'o')
plt.show()