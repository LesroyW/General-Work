from name_function import get_formatted_name

print("Enter 'q' to quit at any time")
while True:
    first = input("\nPlease give me your first name: ")
    if first == 'q':
        break
    middle = input("\nPlease give me your second last: ")
    if middle == "q":
        break
    last = input("\nPlease give me your second last: ")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, middle , last)
    print("So your full name is: " + first + " " + middle + " " + last )
