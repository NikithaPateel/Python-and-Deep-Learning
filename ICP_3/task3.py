import numpy
import scipy
from scipy import stats
from collections import Counter

a = (numpy.random.randint(20, size=15))
print(a)
#print(scipy.stats.mode(a))
#b = numpy.bincount(a).argmax()
#print(b)
co = Counter(a)
for k, v in co.items():
    if v == max(co.values()):
        print(k)



