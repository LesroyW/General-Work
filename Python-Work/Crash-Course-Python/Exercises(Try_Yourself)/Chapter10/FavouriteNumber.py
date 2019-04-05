import json



filename = "StoreNumber.json"




try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
except FileNotFoundError:
    favouriteNumber = input("What is your favourite Number? ")
    with open(filename, 'w') as f_obj:
        json.dump(favouriteNumber, f_obj)
        print("We have stored your favourite number in a file!")
else:
    print("Your favourite number is " + number)
