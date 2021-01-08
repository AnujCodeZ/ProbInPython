from numpy.random import choice
import matplotlib.pyplot as plt

# Generating descrete random variables
print(choice([1, 2, 3], p=[0.2, 0.5, 0.3]))

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

sample = [choice([1, 2, 3], p=[0.2, 0.5, 0.3]) for _ in range(10000)]

print(count_frequencies(sample, relative=True))

# Visualizing
freqs = count_frequencies(sample, relative=True)

plt.bar(freqs.keys(), freqs.values())
plt.show()