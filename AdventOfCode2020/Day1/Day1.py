f = open('Day1Input.txt','r')



numbers_array1 = []

for line in f:
    numbers_array1.append(int(line))

f.close()

for number1 in numbers_array1:                
    if number1 in numbers_array1:
        for number2 in numbers_array1:
            if 2020 - (number1 + number2) in numbers_array1:
                print((2020 - number1 - number2) * number1 * number2)
                break
      

numbers_array = []

for line in f:
    numbers_array.append(int(line))

for number in numbers_array:                
    if 2020 - number in numbers_array:
        print(number * (2020 - number))
        break
f.close()






