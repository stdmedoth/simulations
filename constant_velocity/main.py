import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class ConstantVelocity:
    def __init__(self) -> None:
        self.r = [[0.0],[0.0],[0.0]]
        self.t = [0]
        self.vx = 1.0 # velocity on x component
        self.vy = 1.0 # velocity on y component
        self.vz = 1.0 # velocity on z component
        self.dt = 1   # infinitesimal time

        self.line = 0
        self.point = 0


        self.x = 0
        self.y = 1
        self.z = 2

    def calculate(self):
        for i in range(0,100):
            rx = self.r[self.x][i] 
            ry = self.r[self.y][i]
            rz = self.r[self.z][i]

            drx = self.vx*self.dt
            dry = self.vy*self.dt
            drz = self.vz*self.dt
            
            self.r[self.x].append(rx + drx)
            self.r[self.y].append(ry + dry)
            self.r[self.z].append(rz + drz)
            
            self.t.append(self.t[i] + self.dt)
    
    def animate(self, frame):
        print(frame)
        print(self.r[self.x][frame], self.r[self.y][frame], self.r[self.z][frame])
        self.line[0].set_data_3d([self.r[self.x][frame]], [self.r[self.y][frame]], [self.r[self.z][frame]])
        self.point[0].set_data_3d([self.r[self.x][frame]], [self.r[self.y][frame]], [self.r[self.z][frame]])
        
    def view(self):
        fig  = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_zlim(0, 100)
        ax.set_xlabel("x(t)")
        ax.set_ylabel("y(t)")
        ax.set_zlabel("z(t)")
        
        self.line = ax.plot3D([self.r[self.x][0]],[self.r[self.y][0]],[self.r[self.z][0]])
        self.point = ax.plot3D([self.r[self.x][0]],[self.r[self.y][0]],[self.r[self.z][0]],"o")
        
        an = FuncAnimation(fig, self.animate, frames=100, interval=100)
        plt.show()

    def start(self):
        self.calculate()
        self.view()

cv = ConstantVelocity()
cv.start()