
"""
What will be printed out by this code?

A) (1, 2, [30, 40, 50, 60])
B) 'tuple' object does not support item assignment
C) Nothing
D) Both A and B
"""


t = (1, 2, [30, 40])

try:
    t[2] += [50, 60]
except Exception as e:
    print(str(e))

print(t)
