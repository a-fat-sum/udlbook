import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 2, 0.01)
y = np.exp(x)

plt.figure()
plt.plot(x, y, '.-')
plt.show()

z = 10