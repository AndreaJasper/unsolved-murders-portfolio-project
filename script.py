
import json
import csv

data_set = "homicide_report.csv"

data_file = []

with open(data_set, newline='') as data:
  data_reader = csv.DictReader(data)
  for row in data_reader:
    data_file.append(row)

# with open(data_set, newline='') as data:
#   reader = csv.reader(data, delimiter=' ')
#   for row in reader:
#     data_file.append(', '.join(row))

print(data_file[2])

# how many male v female victims

# how many male v female v unknown perpetrators

# average perpetrator age

# print("Average age of perpetrator is " + round(average))

# state with the most murders

# solved v unsolved

# state with the most

# state with the least

# city with the most

# city with the least

# difference in total deaths from 1980 and 2014