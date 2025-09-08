# Simple algorithms

# Fibonacci numbers
def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        gp = 1
        p = 1
        for _ in range(1,n):
            gp, p = p, p + gp
        return p

# Powerset of a set
def power_set(set):
    if len(set) == 0:
        return [[]]

    all_subsets = [[]]

    for x in set:
        new_subsets = []

        for s in all_subsets:
            s = s[:]
            s.append(x)
            new_subsets.append(s)

        all_subsets.extend(new_subsets)

    return all_subsets

# Exponential growth
def exponential_growth(n, factor, days):
    seq = [n]
    for _ in range(0, days):
        seq.append(seq[-1] * factor)
    return seq




