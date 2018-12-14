# coding: utf-8
import random
import matplotlib.pyplot as plt
from matplotlib import animation
import datetime

fig, ax = plt.subplots()


def generate_x():
    interval = [s for s in range(-5, 6)]
    now_time = datetime.datetime.now()
    dist = datetime.timedelta(minutes=5)
    return [(now_time + dist * s).strftime('%H:%M') for s in interval]


def generate_y():
    return [random.randint(1, 100) for s in range(1, 12)]


line, = ax.plot(generate_x(), generate_y())


def animat(i):
    line.set_xdata(generate_x())
    line.set_ydata(generate_y())
    return line,


def initial():
    line.set_xdata(generate_x())
    line.set_ydata(generate_y())
    return line,


ani = animation.FuncAnimation(fig=fig, func=animat, frames=100, init_func=initial, interval=1000, blit=False)

plt.show()
