import pygal
from rollingDiceTIY import Die

die1 = Die(6)
die2 = Die(6)
die3 = Die(6)


results = []
for roll in range(1000):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides + die3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.x_labels = []
for value in range(3, max_result+1):
    hist.x_labels.append(value)
hist.y_title = "Frequency"
hist.x_title = "Result"
hist.title = "Value of three D6 die rolled 1000 times."

hist.add("D6 + D6 + D6",frequencies)

hist.render_to_file("D6_render_TIY3.svg")