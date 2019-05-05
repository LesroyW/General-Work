import matplotlib.pyplot as plt

#Y axis values
square_value= [1, 4, 9,16,25,36,49]
#X axis values
value = [1,2,3,4,5,6,7]
#Defines the type of graph it is going to be.
plt.scatter(value, square_value, s= 30)
#Provides a label for a title
plt.title("Square Numbers")
#labels the x axis
plt.xlabel("Value for X", fontsize=12)
#Labes the y axis
plt.ylabel("Value for Y", fontsize=14)

plt.tick_params(axis='both', which='major',labelsize=12)

#Shows the graph
plt.show()
