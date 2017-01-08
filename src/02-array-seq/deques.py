from collections import deque

dq = deque([1, 2, 3, 4, 5, 6, 7, 8], maxlen=8)
print(dq)
dq.extend([14, 16])
print(dq)
dq.extendleft([15, 13])
print(dq)
dq.rotate(-2)
print(dq)
