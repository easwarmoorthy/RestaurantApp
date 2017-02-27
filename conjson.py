import json
from pprint import pprint
import json
import csv
e = open('data.csv', 'w')
csvwriter = csv.writer(e)
with open('data.json') as data_file:
    data = json.load(data_file)
for i in range(3):
    pprint(data[i]["name"])
    pprint(data[i]["url"])
    x = data[i]["name"]
    y = data[i]["url"]
    z = data[i]["location"]["city"]
    a = data[i]["location"]["address"]
    csvwriter.writerow([x,y,a,z])
e.close()
