
from numpy import arange
from scipy.stats import hypergeom
import matplotlib.pyplot as plt

(N,K) = (50,30)
n = arange(0, K, 1)
y = hypergeom.pmf(N, K, n) 

plt.plot(x,y, 'bo')
plt.title('Hypergeometric distribution with parameters N = 50, K = 20')
plt.show()




