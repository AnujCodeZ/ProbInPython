from itertools import product

print(list(product([1, 2], ['a', 'b', 'c'])))

n = 3 # number of coin tossings

omega = set(product(['H', 'T'], repeat=n)) # sample space
print(omega)

# Events
A = {o for o in omega if o[0] == 'T'} # first toss is tail
B = {o for o in omega if o.count('T') == 2} # exactly two tails

print(A, B)

# Probability
def prob(X):
    return len(X) / len(omega)

# Consitional probability
def cond_prob(X, Y):
    return len(X & Y) / len(Y)

print(prob(A), prob(B))

print(cond_prob(A, B))

# Independence
def are_indep(X, Y):
    return prob(X & Y) == prob(X) * prob(Y)

print(are_indep(A, B))

C = {o for o in omega if o[1] == 'H'} # second toss is head
print(are_indep(A, C))