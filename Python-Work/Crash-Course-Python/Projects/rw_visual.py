import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:

    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)
    plt.scatter(0,0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolor='none', s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

        #Page 367n