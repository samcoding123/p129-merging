import csv

with open("sorteddata.csv") as input, open("newsorteddata.csv", "w", newline='') as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)
