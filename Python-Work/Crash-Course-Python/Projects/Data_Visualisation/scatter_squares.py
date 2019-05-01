import matplotlib.pyplot as plt

square_value= [1, 4, 9,16,25,36,49]
value = [1,2,3,4,5,6,7]
plt.scatter(value, square_value, s= 100)
plt.title("Square Numbers")
plt.xlabel("Value for X", fontsize=12)
plt.ylabel("Value for Y", fontsize=14)

plt.tick_params(axis='both', which='major',labelsize=12)

plt.show()
