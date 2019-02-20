def make_pizza(size, *toppings):
    print("making a " + str(size) + " sized pizza.")
    for topping in toppings:
        print("- " + topping)
