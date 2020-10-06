import collections
from itertools import permutations

def tilePossiblilites(s):
    d = collections.defaultdict(int)
    for c in s:
        d[c] += 1
    repeated_count = []

    for i in d.values():
        if i >1:
            repeated_count.append(i)
    awesome = []
    for i in range(1, len(s)+1):
        comb = permutations(list(s), i)
        for j in list(comb):
            awesome.append(j)
    return len(set(awesome))
print tilePossiblilites("AAB")
