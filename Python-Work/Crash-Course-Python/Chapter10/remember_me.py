import json



def greet_user():

    username = get_stored_username()
    outcome = input("Is " +username + " your username?")

    if outcome == "Yes":
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember this username for you: " + username + ".")

def get_new_username():
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
        return username


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

greet_user()
