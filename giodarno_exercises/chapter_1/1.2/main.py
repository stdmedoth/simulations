import matplotlib.pyplot as plt

class Velocity:
    def __init__(self):
        self.dt = 0.0
        self.pos = []
        self.time = [0]
        self.vel = 0.0
        self.max_time = 10

    def initialize(self):
        self.dt = 0.1
        self.pos.append(float(input("Input the initial position: ")))
        self.vel = float(input("Input the constant velocity: "))

    def calculate(self):
        for i in range(0, int(self.max_time/self.dt)+1):
            self.pos.append(self.pos[i] + self.vel*self.dt)
            self.time.append(self.time[i]+ self.dt)
            print("time: " + str(self.time[i]) + " " + "pos: "+ str(self.pos[i]))
            if self.time[i] > 0:
                print("Instantaneous velocity: "+str((self.pos[i]-self.pos[0])/(self.time[i]-self.time[0])))

    def view(self):
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.scatter(self.time, self.pos)
        plt.show()


    def start(self):
        self.initialize()
        self.calculate()
        self.view()

v = Velocity()
v.start()