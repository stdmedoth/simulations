import math
import matplotlib.pyplot as plt


class RadioactiveDecay:

    MAX = 100

    def __init__(self):
        self.n_atoms = []
        self.time = []
        self.dt = 0.0
        self.tau = 0.0
        self.t_max = 0.0

    def initialize(self):
        self.n_atoms.append(float(input("Initial number of n_atoms: ")))
        self.tau = float(input("Time constant: "))
        self.dt = float(input("Time step: "))
        self.time.append(0)

    def default_method(self):
        for i in range(self.MAX):
            self.n_atoms.append(
                self.n_atoms[i] - (self.n_atoms[i]/self.tau) * self.dt
                )
            self.time.append(self.time[i] + self.dt)
    
    def euler_method(self):
        for i in range(self.MAX):
            self.n_atoms.append(
                self.n_atoms[0]*pow(math.e, -(self.time[i]/self.tau))
                )
            self.time.append(self.time[i] + self.dt)

    def view(self):
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot()
        self.default_method()
        ax.scatter(self.time, self.n_atoms)
        
        self.n_atoms = [self.n_atoms[0]]
        self.time = [0]
        self.euler_method()
        ax.scatter(self.time, self.n_atoms)
        ax.grid()
        plt.show()

        
    def load(self):
        self.initialize()
        self.view()
        
    

d = RadioactiveDecay()
d.load()
