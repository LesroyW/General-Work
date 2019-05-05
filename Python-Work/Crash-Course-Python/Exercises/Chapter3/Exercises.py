names = ["Simon", "Jeff", "Matt"]

print("Hi my name is " + names[0])
print("I'm " + names[1] + " nice to meet you")
print("What can I do for you?, I'm " + names[2])

peopleIwouldInvite = ["Fernando Alonso", "Barack Obama", "Lewis Hamilton", "Zach Braff"]
print("Come to my party " + peopleIwouldInvite[-1])
print("See you later, " + peopleIwouldInvite[0])
print("Sorry you couldn't make it " + peopleIwouldInvite[1])
print("Hey its you!, " + peopleIwouldInvite[2])
names.insert(0, 'Zachary Fox')
print(names)
names.insert(3, 'Donald Faison')
print(names)
names.append('Phillp Defranco')
print(names)
print("I've only got space for 2 sorry guys")
print("Sorry  " + names.pop())
print("Sorry, " + names.pop())
print("Sorry, " + names.pop())
print("Sorry, " + names.pop())
print("Sorry, " + names.pop())
print("Hey, " + peopleIwouldInvite[0] + " , " + peopleIwouldInvite[1] + ". You guys are still on the list")
del names[0]
print(names)


locations = ["Berlin", "London", "Monte Carlo", "Barcalona", "New York", "Sydney"]
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)
lengthofList = len(locations)
print(lengthofList)
