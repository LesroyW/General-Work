import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Get high temperatures from file.
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[2])
        lows.append(low)

    print(highs)
#Plot data
fig = plt.figure(dpi=128, figsize=(10,20))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')


#Format plot.
plt.title("Daily high tempratures, July 2014", fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.xticks(dates)
plt.ylabel("Temperature(F)", fontsize= 16)
plt.tick_params(axis="both", which='minor', labelsize =16)
plt.show()

#Page 388