"Reading a file"

import csv

with open("full_data.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)
    #print(data)
    #
"Removing Headers from the list"

headers = data[:1]
data = data[1:]
# print(headers)
# print(data[:5])

"Counting gun dates by year"

years=[row[1] for row in data]
#print(years)

guns_count={}

for year in years:
    if year not in guns_count:
        guns_count[year]=0
    guns_count[year]+= 1

#print(guns_count)

"Exploring Gun Deaths By Month And Year"

import datetime
dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]
#print(dates[:5])


date_counts = {}

for date in dates:
    if date not in date_counts:
        date_counts[date] = 0
    date_counts[date] += 1

#print(date_counts)


"Exploring Gun Deaths By Race And Sex"


sexes = [row[5] for row in data]
sex_counts = {}
for sex in sexes:
    if sex not in sex_counts:
        sex_counts[sex] = 0
    sex_counts[sex] += 1
print(sex_counts)



races = [row[7] for row in data]
race_counts = {}
for race in races:
    if race not in race_counts:
        race_counts[race] = 0
    race_counts[race] += 1
race_counts


"Computing Rates Of Gun Deaths Per Race"

mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}
race_per_hundredk = {}
for k,v in race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

print(race_per_hundredk)


intents = [row[3] for row in data]
homicide_race_counts = {}
for i,race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i] == "Homicide":
        homicide_race_counts[race] += 1

race_per_hundredk = {}
for k,v in homicide_race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

print(race_per_hundredk)