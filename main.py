import csv 
data = []
with open("data2.csv") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)
headers=data[0]
planet_data=data[1:]
for datapoint in planet_data:
    datapoint[0]=datapoint[0].lower()
planet_data.sort(key=lambda planet_data:planet_data[0])
with open("data2_sorted.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
