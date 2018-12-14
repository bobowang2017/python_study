# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib import animation

x = [i for i in range(1, 10)]
y = list(map(lambda s: pow(s, 2), x))
data = [x, y]
im = plt.imshow(data, cmap='gray')


def animate(i):
    data = [[s + i for s in x], [s + i for s in y]]
    im.set_array(data)
    print(data)
    plt.plot(data[0], data[1])
    return [im]


fig = plt.figure(figsize=(10, 6))

# plt.figure(figsize=(10, 6))
# plt.plot(x, y)
# plt.xlim(1, 20)
# plt.ylim(1, 100)
anim = animation.FuncAnimation(fig, animate, frames=20, interval=60, blit=True)
plt.show()
