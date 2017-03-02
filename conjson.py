import json
from pprint import pprint
import csv
import time
e = open('data.csv', 'w')
with open('data.json') as data_file:
    data = json.load(data_file)
#    print data
csvwriter = csv.writer(e)
for i in range(4):
    pprint(data[i])
    pprint(data[i]["name"])
    pprint(data[i]["url"])
    x = data[i]["name"]
    y = data[i]["url"]
    z = data[i]["location"]["city"]
    a = data[i]["location"]["address"]
    csvwriter.writerow([x,y,a,z])
e.close()
