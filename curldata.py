import urllib2
import json
from pprint import pprint
import csv
import time
e = open('data.csv', 'w')
csvwriter = csv.writer(e)
class fun(object):
    pass
x = 72000
data = []
while x < 72200:
    site=  "https://developers.zomato.com/api/v2.1/restaurant?res_id=" + str(x)
    hdr = {
    'Accept': 'application/json',
    'user-key': '6aebfe02b9c7820ae965ccf5769fea39',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}
    req = urllib2.Request(site, headers=hdr)
    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()
    content = page.read()
    obj = eval(content)
    try:
        if obj["name"] not in data:
            try:
                data.append(obj["name"])
                if obj["location"]["city_id"] == 7:
                    q = obj["name"]
                    y = obj["url"]
                    z = obj["location"]["city"]
                    a = obj["location"]["address"]
                    csvwriter.writerow([q,y,a,z])
                    print obj["name"]
            except KeyError:
                pass
    except KeyError:
        pass
    x = x + 1
e.close()
# curl -X GET --header "Accept: application/json" --header "user-key: 6aebfe02b9c7820ae965ccf5769fea39" "https://developers.zomato.com/api/v2.1/restaurant?res_id=1"
