import json

favouriteNumber = input("What is your favourite Number? ")

filename = "StoreNumber.json"

with open(filename, 'w') as f_obj:
    json.dump(favouriteNumber, f_obj)
    print("We have stored your favourite number in a file!")

with open(filename) as f_obj:
    number = json.load(f_obj)

print(number)
