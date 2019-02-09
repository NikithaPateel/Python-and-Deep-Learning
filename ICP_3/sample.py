from collections import Counter
import numpy
c = [1, 2, 2, 1, 1, 3, 3, 3]
co = Counter(c)
print(co)
for k, v in co.items():
    if v == max(co.values()):
        print(k)


