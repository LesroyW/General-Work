import csv
from datetime import datetime
from matplotlib import pyplot as plt 


filename = 'fpl_data_2018_2019.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    year, medals, countrys = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[9], '%Y')
        country = row[6]
        medal = row[14]

        if row[10] != "Summer":
            year.append(current_date)
            medals.append(medal)
            countrys.append(country)
    print(len(medals))



#analyse
fig = plt.figure(dpi =128, figsize=(10,6))
plt.plot(year,medals, c='blue')


title = "Medals from the Summer Olympic games"
plt.title(title, fontsize =24)
plt.ylabel("Hi")
plt.xlabel("NO")
plt.tick_params(axis="both", which='major', labelsize=24)
plt.xticks(year)


plt.show()


#format