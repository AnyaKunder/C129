import csv
dataset1=[]
dataset2=[]
with open("final.csv")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset1.append(row)
with open("data2_sorted.csv")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset2.append(row)
headers1=dataset1[0]
planetdata1=dataset1[1:]
headers2=dataset2[0]
planetdata2=dataset2[1:]
headers=headers1+headers2
planet_data=[]
for index,data_row in enumerate(planetdata1):
    planet_data.append(planetdata1[index]+planetdata2[index])
with open("final_data.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
