import matplotlib.pyplot as plt

class FrictionalForce:
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.max_time = 10

        self.v = []
        self.dt = 0.05
        self.time = [0]

    def initialize(self):
        self.a = float(input("Input the acelleration: "))
        self.b = float(input("Input the b constant of bv: "))
        self.v.append(float(input("Input the initial velocity: ")))

    def calculate(self):
        for i in range(0, (int(self.max_time/self.dt)+1)):
            iv = self.v[i] # instantaneous velocity
            riv = (self.a - self.b*iv) # resultant instantaneous velocity 
            dv = riv * self.dt # resultant derivative velocity

            t = self.time[i]
            dt = self.dt


            self.v.append(iv + dv)
            self.time.append(t + dt)

    def view(self):
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.scatter(self.time, self.v)

    def start(self):
        self.initialize()
        self.calculate()
        self.view()
        plt.show()
        
f = FrictionalForce()
f.start()