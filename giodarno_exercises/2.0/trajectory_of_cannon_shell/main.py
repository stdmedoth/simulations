import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class CanonShellTrajectory:
    def __init__(self) -> None:
        self.r = [[0],[0],[0]]
        self.v = [[30],[50],[0]]
        self.a = [[0], [-9.8], [0]]
        
        self.t = [0]
        self.dt = 0.1
        self.x = 0
        self.y = 1
        self.z = 2

    def calculate(self):
        x = 0
        y = 1
        z = 2
        for i in range(0,300): 
            a = self.a
            # velocity euler diferential for velocity
            dvx = (a[self.x][0] * self.dt)
            dvy = (a[self.y][0] * self.dt)
            dvz = (a[self.z][0] * self.dt)
            vx = (self.v[self.x][i] + dvx)
            vy = (self.v[self.y][i] + dvy)
            vz = (self.v[self.z][i] + dvz)
            self.v[self.x].append(vx)
            self.v[self.y].append(vy)            
            self.v[self.z].append(vz)

            # velocity euler diferential for position
            drx = (vx * self.dt)
            dry = (vy * self.dt)
            drz = (vz * self.dt)
        
            rx = (self.r[self.x][i] + drx)
            ry = (self.r[self.y][i] + dry)
            rz = (self.r[self.z][i] + drz)

            self.r[self.x].append(rx)
            self.r[self.y].append(ry)            
            self.r[self.z].append(rz)

    def animate(self, frame):
        print((self.r[self.x][frame], self.r[self.y][frame], self.r[self.z][frame]))
        self.line[0].set_data_3d([self.r[self.x][frame]], [self.r[self.y][frame]], [self.r[self.z][frame]])
        self.point[0].set_data_3d([self.r[self.x][frame]], [self.r[self.y][frame]], [self.r[self.z][frame]]) 

    def view(self):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.set_xlim(0, 300)
        ax.set_ylim(0, 300)
        ax.set_zlim(-300, 300)
        ax.set_xlabel("x(t)")
        ax.set_ylabel("y(t)")
        ax.set_zlabel("z(t)")
        ax.view_init(0, vertical_axis='y')


        self.line = ax.plot3D([self.r[self.x][0]],[self.r[self.y][0]],[self.r[self.z][0]])
        self.point = ax.plot3D([self.r[self.x][0]],[self.r[self.y][0]],[self.r[self.z][0]],"o")

        an = FuncAnimation(fig, self.animate, frames=100, interval=100)
        an.save("animation.gif")
        plt.show()



    def start(self):
        self.calculate()
        self.view()


cst = CanonShellTrajectory()
cst.start()
