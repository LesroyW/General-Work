# % operator is used to format a set of variables enclosed in a "tuple", together with a format string
# for example 
# name = Jeff
# print("Hello %s!" % name) in which %s would correlate to the information stored in the variable name
#To do the same with more variables use a tuple to help here
#Similarly this does not only apply to strings as any object that isnt a string can be formated such as a list
# %s is for string or an object with string representation e.g numbers
# %d is for Integers
# %f is for floating point numbers
# %.<Number of digits>f - floating point numbers with a fixed amount of digits to the right of the dot
# %x/%X - Integers in hex representation
# When using a tuple with string formatting each %s represents each index in the tuple one by one.