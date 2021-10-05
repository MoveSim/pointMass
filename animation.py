from matplotlib import pyplot as plt
from matplotlib import animation


def animate_shit(y_data):
    """"
    Function to animate the bouncing ball, assuming the x position is constant (0).

    :param y_data: list with y positions over the time.
    """

    fig = plt.figure()

    radius = 0.75

    ax = plt.axes(xlim=(-11, 11), ylim=(0, 11))
    ax.set_aspect('equal', adjustable='box')
    ax.plot([-11, 11], [0, 0])
    patch = plt.Circle((0, 11), radius, fc='y')
    ax.add_patch(patch)

    def animate(i):
        x = 0
        y = y_data[i] + radius
        patch.center = (x, y)
        return patch,

    ani = animation.FuncAnimation(fig, animate,
                            frames=len(y_data),
                            interval=1,
                            blit=True)

    plt.show()
