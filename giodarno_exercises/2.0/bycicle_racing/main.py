import matplotlib.pyplot as plt


class BycicleRacing:
    def __init__(self) -> None:
        self.v = [1]
        self.t = [0]
        self.pow = 100.0
        self.m = 1.0
        self.dt = 0.001

    """ as the force function is too dificult to create, maybe we should use power instead of force """
    def calculate(self):
        for i in range(0,100):
            dv = (self.pow/(self.m*self.v[i]))*self.dt
            self.v.append(self.v[i] + dv)
            self.t.append(self.t[i] + self.dt)

    
    def view(self):
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.scatter(self.t, self.v)
        plt.show()

    def start(self):
        self.calculate()
        self.view()


br = BycicleRacing()
br.start()
