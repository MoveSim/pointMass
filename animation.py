from matplotlib import pyplot as plt
from matplotlib import animation


class AnimateShit:
    """"
    Class to animate the bouncing ball, given the x and y positions and the velocity in x and y
    direction.
    """
    def __init__(self, data):
        self.radius = 0.75
        self.x_data = list(data["xpos"])
        self.y_data = [y + self.radius for y in list(data["ypos"])]
        self.vx = list(data["vx"])
        self.vy = list(data["vy"])
        self.fig, self.ax = plt.subplots()
        self.ball = plt.Circle((self.x_data[0], self.y_data[0]), self.radius)
        self.arrow = None

    def set_figure(self):
        self.ax.set_aspect('equal', adjustable='box')
        self.ax.set_xlim(-11, 11)
        self.ax.set_ylim(-.25, 11.75)
        # horizontal limits
        self.ax.plot([-11, 11], [0, 0], c='black')
        self.ax.plot([-10.75, 10.75], [11.5, 11.5], c='b')
        # vertical limits
        self.ax.plot([-10.75, -10.75], [0, 11.5], c='b')
        self.ax.plot([10.75, 10.75], [0, 11.5], c='b')

    def run(self):
        self.set_figure()
        self.ax.add_patch(self.ball)
        ani = animation.FuncAnimation(self.fig, self.animate,
                                      frames=len(self.y_data),
                                      interval=1,
                                      blit=True)

        plt.show()

    def get_arrow(self, i):
        x = self.x_data[i]
        y = self.y_data[i]
        u = self.vx[i]
        v = self.vy[i]
        return x, y, u, v

    def animate(self, frame):
        x = self.x_data[frame]
        y = self.y_data[frame]
        self.ball.center = (x, y)

        self.arrow = plt.Arrow(*self.get_arrow(frame))
        self.ax.add_patch(self.arrow)

        return self.ball, self.arrow


