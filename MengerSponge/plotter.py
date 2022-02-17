import numpy as np
import matplotlib.pyplot as plt
from boxes import Box
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')
numTimes = 2


def recursiveCubeSplit(center, size, numTimes):
    if numTimes == 0:
        return
    b = Box(center, size)
    # x, y, z = b.getEdges()

    sign = [size/3, 0, -1*size/3]
    for i in sign:
        for j in sign:
            for k in sign:
                isCentre = int(i == 0) + int(j == 0) + int(k == 0)

                newcenter = list(center.__add__([i, j, k]))
                newbox = Box(newcenter, size/3)
                x, y, z = newbox.getEdges()
                faces = newbox.getSurfaces()

                if isCentre == 2:
                    for face in faces:
                        face = np.array(face)
                        ax.plot_surface(face[0].reshape(2, 2), face[1].reshape(
                            2, 2), face[2].reshape(2, 2), color='blue')
                else:
                    recursiveCubeSplit(np.array(newcenter), size/3, numTimes-1)

    return


center = np.array([0, 0, 0])
size = 9
recursiveCubeSplit(center, size, 4)
# for angle in range(0, 360, 15):
#     ax.view_init(10, angle)
#     plt.draw()
#     plt.pause(.1)
plt.show()
