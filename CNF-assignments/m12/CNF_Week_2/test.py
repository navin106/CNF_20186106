import csv
reader = csv.reader(open('data.csv', 'r'))
d = {}
for row in reader:
   d[row[0]] = [row[1],row[2]]
print(d['20158501'][0])