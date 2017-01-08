import random
import bisect


grades = 'EDCBAS'
thresholds = [10, 50, 70, 90, 100]


example = [random.randint(0, 100) for _ in range(100)] + [100]

for score in example:
    grade = grades[bisect.bisect(thresholds, score)]
    print('{} --> {}'.format(score, grade))
