#Finding the length of a string using print(len(astring))
#print(astring.index("o")) prints the index location of the first occurance of the letter in the string
#print(astring.count("l")) prints the amount of occurances of a letter within the string
#print(astring[3:7]) prints the letters within the string that correspond to the index boundries
# Skipping character involves using [ Start:stop:step] using a - number for step means x character from the end
# No reverse function but can be done through slice syntax - print(astring[::-1])
# For printing in uppercase and lowercase string.upper and string.lower can be used respectively
# Additionally astring.startswith and astring.endswith returns a bool as it determines wheater the string starts/finishes with something
# astring.split(" ") allows for the spliting of a string at a specific character
# The addition of a number within the split e.g (" " , 1) limits the amount of times the string is split.