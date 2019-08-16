import matplotlib.pyplot as plt

squares = [1,4,9,16,25,36,49]
input_values = [1,2,3,4,5,6,7]
plt.plot(input_values,squares, linewidth = 5)


#Sets the chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

# set the size of tick labels.
plt.tick_params(axis="both", labelsize=14)

plt.show()