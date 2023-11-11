import matplotlib.pyplot as plt
class FreelyFailling:
    def __init__(self):
        self.dt = 0.0
        self.max_time = 0.0
        self.time = [0]
        self.vel = []

    def input(self):
        self.dt = float(input("Time step (s): "))
        self.vel.append(float(input("Initial Velocity (m/s): ")))
        self.max_time = 10.0

    def calculate(self):
        interval = self.max_time/self.dt
        for i in range(0, int(interval)+1):
            self.vel.append(self.vel[i] - 9.8*self.dt)
            self.time.append(self.time[i] + self.dt)
            print("time: " + str(self.time[i]) + " " + "vel: "+ str(self.vel[i]))

    def view(self):
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.scatter(self.time, self.vel)

        plt.show()

    def start(self):
        self.input()
        self.calculate()
        self.view()

ff = FreelyFailling()
ff.start()
