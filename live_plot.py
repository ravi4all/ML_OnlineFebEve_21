import matplotlib.pyplot as plt
import matplotlib.animation as anim

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    file = open('some_data.txt')
    data = file.read()
    file.close()
    x_coord = []
    y_coord = []
    lines = data.split('\n')
    for line in lines:
        x,y = line.split(',')
        x_coord.append(x)
        y_coord.append(y)
    ax1.clear()
    ax1.plot(x_coord,y_coord)

anim = anim.FuncAnimation(fig, animate, interval=1000)
plt.show()
