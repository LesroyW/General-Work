import csv 
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    dates, rainfalls = [],[]
    for row in reader:
        try:
            current_rainfall_time = datetime.strptime(row[0], "%Y-%m-%d")
            rainfall = float(row[19])

        except ValueError:
           print(current_rainfall_time, "Data missing from this date") 

        else:
            dates.append(current_rainfall_time)
            rainfalls.append(rainfall)

    print(rainfalls)  

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates,rainfalls, c='blue')

title = "Rain fall within 1 month"
plt.title(title, fontsize=24)
plt.xlabel("Days", fontsize=16)
fig.autofmt_xdate()
plt.xticks(dates)
plt.ylabel("Rain level in cm", fontsize=12)
plt.tick_params(axis="both", which='minor', labelsize =16)


plt.show()