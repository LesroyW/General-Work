#-----------------------------------------------------------
#Basics of a list

#Example of a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized'] print(bicycles)
#will print out the whole list including the brackets

#Access specific elements in a list similar to java print(list[index])
print(bicycles[0])
#will return the first element in the list
#print(bicycles[0.title()]) will turn captilise the the returned element String

print(bicycles[1])
print(bicycles[3])
#This will return the second and forth element in the list

print(bicycles[-1])
#This will return the last element in the list provided

#Elements can be added within a list
message = "My first bike was " + bicycles[0].title() + "."
print(message)

#-----------------------------------------------------------------
#Addtion, removal and changing og Elements

bicycles[0] = "Mountain"
print(bicycles)
#changes the value of trek to Mountain

#Adding to a list
bicycles.append("trek")
print(bicycles)
#Adds trek to the end of the list
#Can start with an empty list and dynamically add it using append

#Inserting into a list
bicycles.Insert(1, 'Bmx')
print(bicycles)
#Adds the name Bmx to the list at index 1. Shuffling the other elements one position

#Deleting element from the list
del bicycles[1]
print(bicycles)
#removes Bmx from the list of bicycles and shifts every element one position lowerself.
#Can remove from the list using that method

#Using the pop Method

popped_bicycle = bicycles.pop()
#pop in this case refers to the end of the list.
print(bicycles)
print(popped_bicycle)

#Can be used to find the last owned item
bicycles.Insert(1,popped_bicycle)
popped_bicycle = bicycles.pop()
print("The last bicycle I owned was " + popped_bicycle.title() + ".")

#pop can be used anywhere within the list by adding the index within the parentheses.
popped_bicycle = bicycles.pop(0)

#Removing by value
bicycles.remove('redline')
#removes the redline from the list
bicycles.append("redline")
#list items can be assigned to a variable to be used to remove from a list
to_remove = 'redline'
bicycle.remove(to_remove)
print(bicycles)
print("\nA " + to_remove.title() + " is too expensive for me.")
#Remove only removes first occurance of the value if more than one appears then a while loop would be requried.

#Sorting a list - Sorts into alphabetically or numerical order
bicycles.sort()
print(bicycles)

#reverse a sorted list e.g ascending
bicycles.sort(reverse=true)
print(bicycles)

#getting the length of the list
len(bicycles)
