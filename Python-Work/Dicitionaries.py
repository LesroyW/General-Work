# Dicitionaries works with keys and values instead of indexes similar to hashmaps
# Different ways of intialisation e.g
#phonebook = {}
#phonebook["John"] = 938477566
#phonebook["Jack"] = 938377264
#phonebook["Jill"] = 947662781
#print(phonebook)

#phonebook = {
#    "John" : 938477566,
#    "Jack" : 938377264,
#    "Jill" : 947662781
#}
#print(phonebook)

# iterating of a dictionary similar to a list but the order of values stored is not kept
# e.g phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
#for name, number in phonebook.items():
#    print("Phone number of %s is %d" % (name, number))

# removing the key from the dictionary also removes the value from the dictionary can be done using del dicitionary[key] or dictionary.pop(key)