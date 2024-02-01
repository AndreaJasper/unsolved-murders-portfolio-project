
import json
import csv

data_set = "homicide_report.csv"

perp_age_list = []

with open(data_set, newline='') as data:
  data_reader = csv.DictReader(data)
  for row in data_reader:
    perp_age_list.append(row['Perpetrator Age'])

# how many male v female victims

# how many male v female v unknown perpetrators

# average perpetrator age
# age_stripped = []
# for age in perp_age_list:
#   strip_age = age.strip('')
#   age_stripped.append(strip_age)

# print(age_stripped)

# def convert_to_int(input_str):
#   if input_str.isdigit():
#     return int(input_str)
#   else:
#     print("Invlid input.")
#     return None

perp_age = []
# converts string numbers back to integers
# def convert_str_to_int(list):
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