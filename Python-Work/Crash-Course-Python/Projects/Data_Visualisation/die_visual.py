import pygal
from rollingDice import Die


die = Die()
die2 = Die()
results = []
for roll_num in range(100):
    result = die.roll() + die2.roll()
    results.append(result)

frequenices = []
max_result = die.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequenices.append(frequency)

hist = pygal.Bar()


hist.title = "Results of rolng two D6 100 times."
hist.x_labels = ['2','3','4','5','6','7' ,'8' ,'9' ,'10' ,'11','12']
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('D6 + D6', frequenices)
hist.render_to_file('die_visual.svg')