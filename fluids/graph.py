import numpy as np
import matplotlib.pyplot as plt

dynamic2d = np.loadtxt("data/output2.csv",
                delimiter=";", dtype=str)

xlen,ylen,zlen = 10,10,10
dynamic3d = np.reshape(dynamic2d, (xlen,ylen,zlen))

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection='3d')
xarr, yarr, zarr = [],[],[]
for x in range(xlen):
    for y in range(ylen):
        for z in range(zlen):
            value_float = float(dynamic3d[x,y,z])
            value_int = int(value_float)
            if value_int == 1:
                xarr.append(x)
                yarr.append(y)
                zarr.append(z)

print(xarr, yarr, zarr)     
ax.scatter(xarr, yarr, zarr, color='blue', marker='o')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.show()
