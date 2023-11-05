from matrix import Matrix
from fluids import Fluid
import numpy as np
import pandas as pd

import matplotlib.animation
import matplotlib.pyplot as plt


xlen,ylen,zlen = 50,50,50
particles_qnt = 50
frames_qnt = 50

m = Matrix((xlen,ylen,zlen))

x = np.random.randint(particles_qnt, size=(xlen))
y = np.random.randint(particles_qnt, size=(ylen))
z = np.random.randint(particles_qnt, size=(zlen))

f = Fluid(m)
f.add_particles((x,y,z))


for i in range(frames_qnt):
    f.flow()
    newarray = m.data.reshape((2500, 50))
    np.savetxt("data/output"+str(i)+".csv", newarray, delimiter=";")


