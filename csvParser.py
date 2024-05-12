import csv

school = []

with open('Tanmenet/functions1/school.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        school.append(row)

print(school)

with open('Tanmenet/functions1/school.py', 'w') as f:
    f.write("#!/usr/bin/env python3\n\n")
    f.write("school = " + str(school))
