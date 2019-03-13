with open('LearningPython.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

for line in lines:
    print(line.replace("python", "Java").rstrip())

name = input("What is you name? ")
filename = "guest.txt"
with open(filename, "w") as file_object:
    file_object.write(name)

name = input("What is you name? if you want to quit enter q. ")
filename = "guest_book.txt"
while name != 'q':
    name = input("What is you name? if you want to quit enter q. ")
    if name != 'q':
        with open(filename, "a") as file_object:
            file_object.write(name + " has visited us!\n")
        print(name + " has visited us!\n")

response_file = 'Programming_Response.txt'
response = ""
while response != 'q':
    response = input("What do you like about programming?")
    if response != 'q':
        with open(response_file, "a") as file_object:
            file_object.write(response + "\n")
