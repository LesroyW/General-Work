import matplotlib.pyplot as plt
import matplotlib.cm 

x_values = list(range(1001))
y_values = [x**2 for x in x_values]
cmap = matplotlib.cm.get_cmap('Reds')
plt.scatter(x_values, y_values, c=y_values, cmap=cmap, edgecolor="none",s=40)
plt.title("Auto Squares")
plt.xlabel("Value",fontsize=12)
plt.ylabel("Squares of Values", fontsize=12)
#Sets the range for each axis
plt.axis([0,100, 0,10000])

#Shows the graph
plt.show()