from matrix import Matrix
from fluids import Fluid
import numpy as np
import pandas as pd

import matplotlib.animation
import matplotlib.pyplot as plt


particles_qnt = 10
xlen,ylen,zlen = 10,10,10


m = Matrix((xlen,ylen,zlen))

x = np.random.randint(particles_qnt, size =(xlen))
z = np.random.randint(particles_qnt, size =(ylen))
y = np.random.randint(particles_qnt, size =(zlen))

f = Fluid(m)
f.add_particles((x,y,z))


for i in range(10):
    f.flow()
    newarray = m.data.reshape((100, 10))
    np.savetxt("data/output"+str(i)+".csv", newarray, delimiter=";")


