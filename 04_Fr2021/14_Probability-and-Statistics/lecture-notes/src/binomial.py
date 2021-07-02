
from numpy import arange
from scipy.stats import binom
import matplotlib.pyplot as plt

x = arange(0, 50, 1)
y = binom.pmf(x, 50, 0.4) 

plt.plot(x,y, 'bo')
plt.title('Binomial distribution with parameters n = 50, p = 0.4')
plt.show()




