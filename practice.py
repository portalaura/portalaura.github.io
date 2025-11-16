import csv
file=open("test.csv", "r")

details=csv.reader(file)

for rec in details:
    print(rec)