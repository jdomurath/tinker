import numpy as np

x = np.linspace(0, 5, 5)
y = x**2

savetxt('output.txt', y)
