
import math
import csv

data_set = "homicide_report.csv"

perp_age_list = []
state = []
city = []
year_list = []
solved = []
victim_count = []

with open(data_set, newline='') as data:
  data_reader = csv.DictReader(data)
  for row in data_reader:
    perp_age_list.append(row['Perpetrator Age'])
    state.append(row['State'])
    city.append(row['City'])
    year_list.append(row['Year'])
    solved.append(row['Crime Solved'])
    victim_count.append(row['Victim Count'])


# locates any age fields that are empty
for i, num in enumerate(perp_age_list):
    if not num.isdigit():
        print(i, num)

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
# print(victim_count)
# print(state)

def create_dictionary(perp_age_list, state, city, year_list, solved, victim_count):
  crimes = dict()
  num_crimes = len(perp_age_list)
  for i in range(num_crimes):
    crimes[perp_age_list[i]] : {'Perpetrator Age': perp_age_list[i],
                                'State': state[i],
                                'City': city[i],
                                'Year': year_list[i],
                                'Crime Solved': solved[i],
                                'Victim Count': victim_count[i]
                                }
  return crimes

crimes = create_dictionary(perp_age_list, state, city, year_list, solved, victim_count)
print(crimes)

# for row in zipped_state:


# victim_to_state = {key: value for key, value in zipped_state}
# print("Victims per sate are: " + str(victim_to_state))


# state with the least

# city with the most

# city with the least

# difference in total deaths from 1980 and 2014