import pygal
from rollingDiceTIY import Die

die1 = Die(10)
die2 = Die(10)


results = []
for roll in range(1000):
    result = die1.roll() * die2.roll()
    print(result)
    results.append(result)

frequencies = []
max_result = die1.num_sides * die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.x_labels = []
for value in range(2, max_result+1):
    hist.x_labels.append(value)
hist.y_title = "Frequency"
hist.x_title = "Result"
hist.title = "Value of two D10 die multiplied rolled 1000 times."

hist.add("D10 x D10",frequencies)

hist.render_to_file("D10_render_TIY.svg")
