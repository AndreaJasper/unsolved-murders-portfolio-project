
import json
import csv

data_set = "homicide_report.csv"

perp_age_list = []

with open(data_set, newline='') as data:
  data_reader = csv.DictReader(data)
  for row in data_reader:
    perp_age_list.append(row['Perpetrator Age'])



perp_age = []
for num in perp_age_list:
  num_str = int(num)
  perp_age_int = num_str

  perp_age.append(perp_age_int)

  print(perp_age)
# average_perp_age = perp_age_int/len(perp_age)
# print("Average age of perpetrator is " + str(average_perp_age))

# state with the most murders

# solved v unsolved

# state with the most

# state with the least

# city with the most

# city with the least

# difference in total deaths from 1980 and 2014