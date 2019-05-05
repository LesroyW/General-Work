import matplotlib.pyplot as plt
import matplotlib.cm

x_values = list(range(5000))
y_values = [x**3 for x in x_values]
cmap = matplotlib.cm.get_cmap('Reds')
plt.scatter(x_values, y_values, c=y_values, cmap=cmap,s=12)
plt.title("Cube Numbers")
plt.xlabel("Values", fontsize =11)
plt.ylabel("Squares of values", fontsize=11)

plt.show()