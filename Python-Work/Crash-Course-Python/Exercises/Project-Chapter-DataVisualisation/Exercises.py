import matplotlib.pyplot as plt

x_values = list(range(5000))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, s=12)
plt.title("Cube Numbers")
plt.xlabel("Values", fontsize =11)
plt.ylabel("Squares of values", fontsize=11)

plt.show()