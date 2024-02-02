
import math
import csv

data_set = "homicide_report.csv"

perp_age_list = []

with open(data_set, newline='') as data:
  data_reader = csv.DictReader(data)
  for row in data_reader:
    # row['Perpetrator Age'] = int(row['Perpetrator Age'])
    perp_age_list.append(row['Perpetrator Age'])


# locates any age fields that are empty
# for i, num in enumerate(perp_age_list):
#     try:
#         int(num)
#     except:
#         print(i, num)

# changes perpetrator age fromstring to int
perp_age = []
for num in perp_age_list:
  num_int = int(num)
  perp_age_int = num_int
  perp_age.append(perp_age_int)

# sum of perpetrators ages
avg_perp_age = 0
for age in perp_age:
  avg_perp_age += age

#average perpetrator age
average_perp_age = avg_perp_age/len(perp_age)
print("Average age of perpetrator is " + str(math.floor(average_perp_age)))

# state with the most murders

# solved v unsolved

# state with the most

# state with the least

# city with the most

# city with the least

# difference in total deaths from 1980 and 2014