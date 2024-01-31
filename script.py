
import json
import csv

filename = "homicide_report.csv"

perp_age = []
victim_sex = []
state_deaths = []
city_deaths = []
years = []

with open(filename, newline='') as data:
  # for line in csv.DictReader(data):
  #   print(line)

  data_reader = csv.DictReader(data)

  for data_row in data_reader:
    perp_age.append(data_row['Perpetrator Age'])
    victim_sex.append(data_row['Victim Sex'])
    state_deaths.append(data_row['State'])
    city_deaths.append(data_row['City'])
    years.append(data_row['Year'])


# how many male v female victims

# how many male v female v unknown perpetrators

# average perpetrator age
def average_age(age):
  return sum(age)/len(age)

average = average_age(perp_age)
print("Average age of perpetrator is " + round(average))

# state with the most murders

# solved v unsolved

# state with the most

# state with the least

# city with the most

# city with the least

# difference in total deaths from 1980 and 2014