import matplotlib.pyplot as plt

#Gets a list of x_values
x_values = list(range(1,100))

#Loops through x list
y_values = [x**2 for x in x_values]

#Produces a scatter graph
plt.scatter(x_values, y_values, s=40, edgecolors="none", c=y_values, cmap=plt.cm.Blues)
plt.title("Auto Squares")
plt.xlabel("Value",fontsize=12)
plt.ylabel("Squares of Values", fontsize=12)
#Sets the range for each axis
plt.axis([0,100, 0,10000])

#Shows the graph
plt.savefig("square_plot.png", bbox_inches="tight")