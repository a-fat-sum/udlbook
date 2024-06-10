import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1000000)
y = np.log(1+x)

plt.figure()
plt.plot(x,y)
plt.show()

z = 10