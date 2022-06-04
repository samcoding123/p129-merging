import csv
data=[]

with open("archive_dataset.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)

headers=data[0]
planetdata=data[1:]
planetdata.sort(key=lambda planetdata:planetdata[2])

with open("sorteddata.csv", "a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)