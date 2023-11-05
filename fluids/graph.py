import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


frames_qnt = 50
dynamic2d = np.loadtxt("data/output1.csv",
                delimiter=";", dtype=str)

xlen,ylen,zlen = 50,50,50
dynamic3d = np.reshape(dynamic2d, (xlen,ylen,zlen))

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection='3d')
ax.grid()


def gen(dynamic3d):
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
    return (xarr, yarr, zarr)


vectors = gen(dynamic3d)
sc = ax.scatter(vectors[0], vectors[1], vectors[2], color='blue', marker='o')

def  sc_format():
    ax.axis('equal')

    ax.set_xlabel('X-axis')
    ax.set_xlim3d(1,xlen)

    ax.set_ylabel('Y-axis')
    ax.set_ylim3d(1,ylen)

    ax.set_zlabel('Z-axis')
    ax.set_zlim3d(1,zlen)

def update(frame):
    dynamic2d = np.loadtxt("data/output"+str(frame)+".csv",
                delimiter=";", dtype=str)

    dynamic3d = np.reshape(dynamic2d, (xlen,ylen,zlen))
    vectors = gen(dynamic3d)
    ax.clear()
    sc_format()
    ax.scatter(vectors[0], vectors[1], vectors[2], color='blue', marker='o')
    
    print("frame: " + str(frame))

sc_format()
ani = animation.FuncAnimation(fig, update,repeat=False, interval=10, frames=range(1,frames_qnt))
#ani.save('videos/animation.gif')

plt.show()
