with open('LearningPython.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

for line in lines:
    print(line.replace("python", "Java").rstrip())
#--------------------------------------------------------------------------------------------------------------------------#
name = input("What is you name? ")
filename = "guest.txt"
with open(filename, "w") as file_object:
    file_object.write(name)
#--------------------------------------------------------------------------------------------------------------------------#
name = input("What is you name? if you want to quit enter q. ")
filename = "guest_book.txt"
while name != 'q':
    name = input("What is you name? if you want to quit enter q. ")
    if name != 'q':
        with open(filename, "a") as file_object:
            file_object.write(name + " has visited us!\n")
        print(name + " has visited us!\n")
#--------------------------------------------------------------------------------------------------------------------------#
response_file = 'Programming_Response.txt'
response = ""
while response != 'q':
    response = input("What do you like about programming?")
    if response != 'q':
        with open(response_file, "a") as file_object:
            file_object.write(response + "\n")
#--------------------------------------------------------------------------------------------------------------------------#
#error catching

print("\nBefore starting please ensure you enter values not text.")
first_number = input("First number to add: ")
second_number = input("Second number to add: ")
try:
    print(int(first_number) +int(second_number))
except ValueError:
    print("PLEASE ENTER A NUMBER NEXT TIME!")

def read_File(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
            print(contents)
    except FileNotFoundError:
        print("Cannot find " + filename + " in this directory")

files = ["cats.txt", "dogs.txt"]
for file in files:
    read_File(file)
#--------------------------------------------------------------------------------------------------------------------------#
