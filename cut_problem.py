from functools import  lru_cache
from collections import defaultdict
from icecream import ic
prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 33]
length_to_price = defaultdict(int)

for i, p in enumerate(prices): length_to_price[i+1] = p

def revenue(n, cache={}, solution={}):
    if n in cache: return cache[n], solution[n]

    canadidate = [ (length_to_price[n], (n, 0)) ]

    for s in range(1, n):
        split = (revenue(s, cache, solution)[0] + revenue(n-s, cache, solution)[0], (s, n-s) )
        canadidate.append(split)

    optimal, optimal_split = max(canadidate, key=lambda x: x[0])
    cache[n] = optimal
    ic(optimal)
    solution[n] = optimal_split

    return optimal, solution

optimal, solution = revenue(10)
#ic(optimal)
ic(solution)

