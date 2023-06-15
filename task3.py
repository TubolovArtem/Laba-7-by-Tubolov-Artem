import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-3 * np.pi, 3 * np.pi, 1000)

y = np.cos(x)
z = x / np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z)


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Вариант 8')


plt.show()
