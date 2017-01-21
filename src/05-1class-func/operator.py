from operator import add, mul, itemgetter
from functools import reduce, partial

# some examples from the operator module

# the number of squares in a chess board
print(reduce(add, (x ** 2 for x in range(8))))

# sorting tabular data
data = [
    (17, 'Rocket Launcher', 7, 'Marines'),
    (12, 'Rifle', 14, 'Marines'),
    (22, 'Sniper Rifle', 3, 'Marines'),
    (16, 'Machine Gun', 8, 'Marines'),
    (17, 'Rocket Launcher', 12, 'Green Berets'),
    (12, 'Rifle', 22, 'Green Berets'),
    (22, 'Sniper Rifle', 1, 'Green Berets'),
    (16, 'Machine Gun', 3, 'Green Berets'),
]

for row in sorted(data, key=itemgetter(3, 2)):
    print(row)

# times 5!!

quintuple = partial(mul, 5)
print(' '.join(list(map(str, map(quintuple, range(5))))))

